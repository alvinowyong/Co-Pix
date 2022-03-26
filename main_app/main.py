import load
import s2t

# uncomment this for camera
# import camera

import upload
import led

# button trigger here? or start startight
s2t.speech_to_text(1)  #change recording time accordingly

#take a photo here

# uncomment this for camera
# camera.take_photo()

result = upload.emotion_recognition()

print(result)

if (result == 'happiness'):
    print('green')
#      led.green_led()
    
else:
    print('red')
#      led.red_led()




