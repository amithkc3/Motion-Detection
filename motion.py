from picamera import PiCamera
from time import sleep
import numpy as np
from matplotlib import pyplot as plt

threshold = 30

def rgb2gray(img):
    return np.dot(img[...,:3],[0.299,0.587,0.114])


with PiCamera() as camera:
    camera.resolution = (160,128)
    camera.framerate = 24
    sleep(1)

    print("captured background")
    background = np.empty((128,160,3),dtype=np.uint8)
    camera.capture(background,'rgb')
    background_gray = rgb2gray(background)


    img_color = np.empty((128,160,3),dtype=np.uint8)
    img_gray = np.empty((128,160),dtype=np.uint8)
    diff = np.empty((128,160),dtype=np.uint8)
    pixels = 0
    count=0
    try:
        camera.start_preview()
        while(True):
            print("Captured:"+str(count))
            count+=1
            camera.capture(img_color,'rgb')
            img_gray = rgb2gray(img_color)
            diff = np.absolute(background_gray-img_gray)

            diff2 = np.where(diff>threshold,1,0)
            pixels = len(diff2[diff2>0])
            print(pixels)
            
            if(pixels > 100):
                camera.start_recording("clips.h264")
                camera.wait_recording(10)
                camera.stop_recording()
                break

            sleep(0.1)        
    finally:
        camera.stop_preview()
        print("Exiting")
        

  
   

    
