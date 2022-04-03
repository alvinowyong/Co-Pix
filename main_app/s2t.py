import speech_recognition as sr
import led
from datetime import datetime

def speech_to_text(count):
    recognizer = sr.Recognizer()

    # Recording the sound
    with sr.Microphone() as source:
        print("[" + str(datetime.now().time()) + ": Log - Speech-to-Text]: Adjusting to account for ambient noise")
        
        # Adjust energy threshold dynamically to account for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        # Listen for input from microphone
        # Timeout when input stops for parameter{count} number of seconds
        led.indicate()
        print("[" + str(datetime.now().time()) + ": Log - Speech-to-Text]: Listening now...") 
        recorded_audio = recognizer.listen(source, timeout=1)
        
    # Attempt to decode speech into text
    try:
        print("[" + str(datetime.now().time()) + ": Log - Speech-to-Text]: Decoding speech into text")
        text = recognizer.recognize_google(
            recorded_audio,
            language="en-US"
        )
        print("[" + str(datetime.now().time()) + ": Log - Speech-to-Text]:", text)
        led.success()
        return text
    except Exception as ex:
        print("[" + str(datetime.now().time()) + ": Error - Speech-to-Text]: Error occured while decoding speech")
        led.error()
        speech_to_text(2)
