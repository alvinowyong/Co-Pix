import os
import requests
import urllib.request
import time

nouns = open("nouns.txt","r")

AUTHENTICATION_BASE = 'https://api.flaticon.com/v3/app/authentication'
API_SECRET = os.environ.get("FLATICON_KEY")


key = {'apikey': API_SECRET}
token = requests.post(AUTHENTICATION_BASE, data=key).json()['data']['token']

headers = {
    'Accept':'application/json',
    'Authorization':'Bearer ' + token 
}

for i, word in enumerate(nouns):
    if i < 6121:
        continue
    word = word.strip().replace("-","%20")
    if os.path.isfile("C:/Users/alvin/Documents/Co-Pix/natural-language-processing/nouns/" + word + ".png"):
        print(str(i) + '/' + str(11060) + " existing img found: " + word)
        continue
    
    failed = True
    while failed:
        try:
            r = requests.get('https://api.flaticon.com/v3/search/icons/added?q=' + word, headers=headers)
            failed = False
        except Exception as e:
            print("Error fetching data... Retrying.")
            time.sleep(2)
            err = e
            continue

    data = r.json()['data']
    if len(data) > 0:
        print(str(i) + '/' + str(11060) + " found: " + word)
        url = data[0]['images']['64']
        urllib.request.urlretrieve(url, "C:/Users/alvin/Documents/Co-Pix/natural-language-processing/nouns/" + word + ".png")
    else:
        print(str(i) + '/' + str(11063) + " not found: " + word)