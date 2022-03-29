import speech_recognition as sr

def speech_to_text(count):
    recognizer = sr.Recognizer()

    # Recording the sound
    with sr.Microphone() as source:
<<<<<<< Updated upstream
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording Started".format(count))
        recorded_audio = recognizer.listen(source, timeout=count)
        print("Recording Ended")
=======
        print("[Log - Speech-to-Text]: Adjusting to account for ambient noise")
        
        # Adjust energy threshold dynamically to account for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        # Listen for input from microphone
        # Timeout when input stops for parameter{count} number of seconds
        print("[Log - Speech-to-Text]: Listening now...")
        recorded_audio = recognizer.listen(source, timeout=count)
>>>>>>> Stashed changes

    # Attempt to decode speech into text
    try:
<<<<<<< Updated upstream
=======
        print("[Log - Speech-to-Text]: Decoding speech into text")
>>>>>>> Stashed changes
        text = recognizer.recognize_google(
            recorded_audio,
            language="en-US"
        )
        print("[Log - Speech-to-Text]:", text)
        return text
    except Exception as ex:
        print("[Error - Speech-to-Text]: Error occured while decoding speech")
