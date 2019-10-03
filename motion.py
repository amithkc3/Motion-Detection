import picamera
from time import sleep
import numpy as np
import io
import sys
from datetime import datetime as dtime


def get_datestamp():
    return str(dtime.now().__format__("%d-%m-%Y")) + str(".h264")
    
def rgb2gray(img):
    return np.dot(img[...,:3],[0.299,0.587,0.114])
    ##  convert rgb image to gray by dot product with constants 


def write_to_file(stream,filename):
    print("writing to file")
    with stream.lock:
        for frame in stream.frames:
            if(frame.frame_type == picamera.PiVideoFrameType.sps_header):
                stream.seek(frame.position)
                break
                
    try:
        print("wrote to file")
        with io.open("clips/"+str(filename),'ab') as output:
            output.write(stream.read())
    except:
        print("Couldnot open file!!!"+str(filename))
    ##  get location of first frame from the buffer and
    ##  write the whole h264 video object to given file(in append binary mode)
        

def main(preview="no",filename=get_datestamp(),resolution='320x240',length_of_recording=10,number_of_pixels=50,threshold=30):
    res = str(resolution)
    res_list = list(map(int,res.split('x')))
    if(res_list[0] and res_list[1]):
        resolution_r = res_list[1]
        resolution_c = res_list[0]
    else:
        resolution_r = 128
        resolution_c = 160

    preview = str(preview)
    length_of_recording = int(length_of_recording)
    number_of_pixels = int(number_of_pixels)
    threshold = int(threshold)
    
        
    with picamera.PiCamera() as camera:
        camera.resolution = (resolution_c,resolution_r)
        camera.framerate = 20
        camera.annotate_text_size = 12
        output_stream = picamera.PiCameraCircularIO(camera,seconds=length_of_recording)
        sleep(1)
        ##  setup camera
        
        print("captured background")
        background = np.empty((resolution_r,resolution_c,3),dtype=np.uint8)
        camera.capture(background,'rgb',use_video_port=True)
        background_gray = rgb2gray(background)
        ##  get background

        img_color = np.empty((resolution_r,resolution_c,3),dtype=np.uint8)
        img_gray = np.empty((resolution_r,resolution_c),dtype=np.uint8)
        diff = np.empty((resolution_r,resolution_c),dtype=np.uint8)
        
        
        try:
            if(preview == "preview"):
                camera.start_preview()
            while(True):
                pixels = 0
                camera.capture(img_color,'rgb',use_video_port = True)
                img_gray = rgb2gray(img_color)
                diff = np.absolute(background_gray-img_gray)

                diff2 = np.where(diff>threshold,1,0)
                pixels = len(diff2[diff2>0])
                print(pixels)
                ##  subtract image from background and
                ##  get number of pixels above pixel threshold
                
                if(pixels > number_of_pixels):
                    print("Motion detected")
                    output_stream.clear()
                    camera.start_recording(output_stream,format='h264')
                    start = dtime.now()

                    while( (dtime.now() - start).seconds < length_of_recording):
                        camera.annotate_text = dtime.now().__format__("%H:%M:%S-%d/%m/%Y")
                        camera.wait_recording(1)
                        
                    camera.stop_recording()
                    write_to_file(output_stream,filename)

                    camera.capture(img_color,'rgb',use_video_port = True)
                    img_gray = rgb2gray(img_color)
                ##  if number of pixels is large enough record video and save

####Added
#                else:
                    background_gray = (img_gray)                     
                     
        finally:
            if(preview == "preview"):
                camera.stop_preview()
            print("Exiting")
            

if __name__ == "__main__":
    if(len(sys.argv) == 7):
        main(preview=sys.argv[1],filename=sys.argv[2],resolution=sys.argv[3],length_of_recording=sys.argv[4],number_of_pixels=sys.argv[5],threshold=sys.argv[6])
    elif(len(sys.argv) == 6):
        main(preview=sys.argv[1],filename=sys.argv[2],resolution=sys.argv[3],length_of_recording=sys.argv[4],number_of_pixels=sys.argv[5])
    elif(len(sys.argv) == 5):
        main(preview=sys.argv[1],filename=sys.argv[2],resolution=sys.argv[3],length_of_recording=sys.argv[4])
    elif(len(sys.argv) == 4):
        main(preview=sys.argv[1],filename=sys.argv[2],resolution=sys.argv[3])
    elif(len(sys.argv) == 3):
        main(preview=sys.argv[1],filename=sys.argv[2])
    elif(len(sys.argv) == 2):
        main(preview=sys.argv[1])
    else:
        main()
    
       

        
