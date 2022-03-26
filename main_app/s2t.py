import speech_recognition as sr

def speech_to_text(count):

    recognizer = sr.Recognizer()

    ''' recording the sound '''

    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for {} seconds".format(count))
        recorded_audio = recognizer.listen(source, timeout=count)
        print("Done recording")

    ''' Recognizing the Audio '''
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
            recorded_audio,
            language="en-US"
        )
        print("Decoded Text : {}".format(text))
        return text

    except Exception as ex:
        print(ex)
