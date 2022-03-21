import json, os, requests
import base64
from types import SimpleNamespace


def byte_array(l):
    with open(l, "rb") as image:
        str = base64.b64encode(image.read())
        return bytearray(str)


subscription_key = '<>'

face_api_url = "https://cs460.cognitiveservices.azure.com/" + '/face/v1.0/detect'

# replace with picamera function
image_url = 'https://cs460.blob.core.windows.net/cs460blob/yllee.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'overload': 'stream',
    'detectionModel': 'detection_01',
    'returnFaceId': 'false',
    'returnFaceAttributes': 'emotion'
}

body = {'url': image_url}


response = requests.post(face_api_url, params=params,
                         headers=headers, json=body)

# print(json.dumps(response.json()))
data = json.dumps(response.json())
# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print("%s%s" % ("anger: ", x[0].faceAttributes.emotion.anger))
print("%s%s" % ("contempt: ", x[0].faceAttributes.emotion.contempt))
print("%s%s" % ("disgust: ", x[0].faceAttributes.emotion.disgust))
print("%s%s" % ("fear: ", x[0].faceAttributes.emotion.fear))
print("%s%s" % ("happiness: ", x[0].faceAttributes.emotion.happiness))
print("%s%s" % ("neutral: ", x[0].faceAttributes.emotion.neutral))
print("%s%s" % ("sadness: ", x[0].faceAttributes.emotion.sadness))
print("%s%s" % ("surprise: ", x[0].faceAttributes.emotion.surprise))
