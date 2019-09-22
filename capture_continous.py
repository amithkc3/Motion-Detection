from picamera import PiCamera
from time import sleep
import io

stream = io.BytesIO()
with PiCamera() as camera:
    camera.resolution = (320,240)
    sleep(2)
    camera.start_preview()
    camera.start_recording('./stream3.h264')#,format='h264',quality=23)
    camera.wait_recording(10)
    camera.stop_recording()
    camera.stop_preview()
    
