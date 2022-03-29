import os
import requests
import urllib.request
import time

nouns = open("nouns.txt","r")

AUTHENTICATION_BASE = 'https://api.flaticon.com/v3/app/authentication'
# API_SECRET = os.environ.get("FI_KEY")
API_SECRET = '6081cfc5d10169be4b27c8368a1a9c4297037ffd'
# 6081cfc5d10169be4b27c8368a1a9c4297037ffd
# c80f3753fa1bea62e037d8e53bf9ae110ed1ab80
# b938bc7f4e18f5b35ca24d4ff980a5a787d84e04
# ff24c61fcf97f6fc14c03a98f97d733589e5bc02
# 77e608e6995a785a0c5c8e80dd4e1fb302e5dda4
# 55b3a97f3ead5d864eb0b40b263bfdee0d978a4e
# 276597cc6a1362345754bc5f3e7f4d7b64676150
# 618fdf4ddb298ca57b7755ebbfffc22359f17266
# 5e9c0a466f883763622627441f9df53e5628d2f1
# bb9b535ac86273406db7f82e0e27629a02e25e90
# e680997210be60567a63e05b7fef495eafadc1f5
# 6e05d209d4ffd9089cc07ebb66adb28bb7ecf798
# 06ee90e6b7ac4df74fe615765737de9ba4e5d7aa
# c94a8a77287d4c805af8175c7eebfd37942fb5f9
# 6bd8f0b14dba459009ae615dfa117e5bcf26fce0

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