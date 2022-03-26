
from picamera import PiCamera
from time import sleep

def take_photo():
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/data/image.jpg')
    camera.stop_preview()
