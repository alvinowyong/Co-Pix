import load
import s2t
import camera
import upload
import led

"""
The landing point of solution (Co-Pix) - running sequentially using one thread.
Future iterations may consider using alternative multi-processing library
to overcome GIL restrictions so as to run FER and Speech-to-Text concurrently.

Note: Alternatively, threading library can be utilised during speech processing while
executing FER API calls/
"""


def main_app():
    # Reset LED indicators before processing new requests
    led.off_leds()

    # Activate speech-to-text function
    s2t.speech_to_text(2)

    # Take a photo using camera module
    camera.take_photo()

    # Fetch image from data folder
    # Upload image blob to Azure and call to Emotion Recognition API
    result = upload.emotion_recognition()

    # Log FER results into console
    print("[Log- FER Result]:", result)

    # Enable LED based on FER results
    if (result == 'happiness'):
        led.green_led()
    else:
        led.red_led()
