import json, os, requests
import base64
from types import SimpleNamespace
from load import azure_subscription_key, face_api_url


def byte_array(l):
    with open(l, "rb") as image:
        str = base64.b64encode(image.read())
        return bytearray(str)


def get_emotion(image_url):
    subscription_key = azure_subscription_key

    # replace with picamera function
    # image_url = 'https://cs460.blob.core.windows.net/cs460blob/yllee.jpg'
    print(subscription_key)
    print(image_url)
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'overload': 'stream',
        'detectionModel': 'detection_01',
        'returnFaceId': 'true',
        'returnFaceAttributes': 'emotion'
    }

    body = {'url': image_url}

    response = requests.post(face_api_url, params=params,
                             headers=headers, json=body)
    # print(json.dumps(response.json()))
    data = json.dumps(response.json())
    print(data)
    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    dict = {"anger": x[0].faceAttributes.emotion.anger, "contempt": x[0].faceAttributes.emotion.contempt,
            "disgust": x[0].faceAttributes.emotion.disgust, "fear": x[0].faceAttributes.emotion.fear,
            "happiness": x[0].faceAttributes.emotion.happiness, "neutral": x[0].faceAttributes.emotion.neutral,
            "sadness": x[0].faceAttributes.emotion.sadness, "surprise": x[0].faceAttributes.emotion.surprise}
    return str(max(dict, key=dict.get))

    # print("%s%s" % ("anger: ", x[0].faceAttributes.emotion.anger))
    # print("%s%s" % ("contempt: ", x[0].faceAttributes.emotion.contempt))
    # print("%s%s" % ("disgust: ", x[0].faceAttributes.emotion.disgust))
    # print("%s%s" % ("fear: ", x[0].faceAttributes.emotion.fear))
    # print("%s%s" % ("happiness: ", x[0].faceAttributes.emotion.happiness))
    # print("%s%s" % ("neutral: ", x[0].faceAttributes.emotion.neutral))
    # print("%s%s" % ("sadness: ", x[0].faceAttributes.emotion.sadness))
    # print("%s%s" % ("surprise: ", x[0].faceAttributes.emotion.surprise))
