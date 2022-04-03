from picamera import PiCamera
import time

"""
Initialise PiCamera module to capture image of users.
Future iterations may consider the utilisation of dynamically capturing
snapshots at regular intervals.

Alternatively, a more resource heavy implementation can utilise
video streams of a few seconds for analysis.
"""

camera = PiCamera()

# Snap photo and save to data folder as image.jpg
def take_photo():
#     preview(2)
    camera.capture('data/image.png')

# Display view of camera in a window box
def preview(duration):
    camera.resolution = (2592, 1944)
    camera.start_preview()
    time.sleep(duration)
    camera.stop_preview()
