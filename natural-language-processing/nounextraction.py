import os
from nltk.stem import PorterStemmer
from tkinter import *
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
import nltk
import requests
import enchant

english_dictionary = enchant.Dict("en_US")
BASE_ENDPOINT = 'https://api.iconfinder.com/v4/'
API_SECRET = os.environ.get("ICON_API_SECRET")

porter = PorterStemmer()
txt = """Once upon a time there were three little pigs and the time came for them to leave home and seek their fortunes. Before they left, their mother told them " Whatever you do , do it the best that you can because that's the way to get along in the world. The first little pig built his house out of straw because it was the easiest thing to do. The second little pig built his house out of sticks. This was a little bit stronger than a straw house. The third little pig built his house out of bricks. One night the big bad wolf, who dearly loved to eat fat little piggies, came along and saw the first little pig in his house of straw. He said "Let me in, Let me in, little pig or I'll huff and I'll puff and I'll blow your house in!" "Not by the hair of my chinny chin chin", said the little pig. But of course the wolf did blow the house in and ate the first little pig. The wolf then came to the house of sticks. "Let me in ,Let me in little pig or I'll huff and I'll puff and I'll blow your house in" "Not by the hair of my chinny chin chin", said the little pig. But the wolf blew that house in too, and ate the second little pig. The wolf then came to the house of bricks. " Let me in , let me in" cried the wolf "Or I'll huff and I'll puff till I blow your house in" "Not by the hair of my chinny chin chin" said the pigs. Well, the wolf huffed and puffed but he could not blow down that brick house. But the wolf was a sly old wolf and he climbed up on the roof to look for a way into the brick house. The little pig saw the wolf climb up on the roof and lit a roaring fire in the fireplace and placed on it a large kettle of water. When the wolf finally found the hole in the chimney he crawled down and KERSPLASH right into that kettle of water and that was the end of his troubles with the big bad wolf. The next day the little pig invited his mother over . She said "You see it is just as I told you. The way to get along in the world is to do things as well as you can." Fortunately for that little pig, he learned that lesson. And he just lived happily ever after!"""
is_noun = lambda pos: pos[:2] == 'NN'
tokenized = nltk.word_tokenize(txt)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
noun_set = set(nouns)

found = {}
# Converting nouns to imagery
for i, word in enumerate(noun_set):
    if (not english_dictionary.check(word)):
        continue
    url = "https://api.iconfinder.com/v4/icons/search?query=" + word + "&count=1&premium=0"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + API_SECRET
    }

    try:
        response = requests.request("GET", url, headers=headers)
        url = response.json()['icons'][0]['raster_sizes'][3]['formats'][0]['preview_url']
        found[word] = url
        print(url)
    except Exception as err:
        print(str(i) + ". An error occured:", err)
        continue

for word in tokenized:
    if word in found.keys():
        print(word, end=" ")
        print(found[word])
    else:
        print(word, end=" ")

for sentence in nltk.sent_tokenize(txt):
    wordcount = len(nltk.word_tokenize(sentence))
    for i, word in enumerate(nltk.word_tokenize(sentence)):
        if (i == wordcount - 2):
            if word in found.keys():
                print(word, end=" ")
                print(found[word])
            else:
                print(word)
        else:
            if word in found.keys():
                print(word, end=" ")
                print(found[word])
            else:
                print(word, end=" ")
    print()
    print()

root = Tk()
root.title("Co-Pix")
root.geometry("1000x600")
root.iconbitmap("copix_small.ico")

T = Text(root, height=5, width=52)

l = Label(root, text="Fact of the Day")
l.config(font=("Courier", 14))

# myLabel2 = Label(root, text="<images here>", wraplength=900, justify="center")
# response = requests.get("https://cdn3.iconfinder.com/data/icons/business-and-education-1/512/255_book_lesson_study_literature_reading-32.png")
photo = ImageTk.PhotoImage(Image.open("520x520.png"))
img = Label(image=photo)
img.image = photo

l.pack()
T.pack()
# img.pack()
# myLabel2.pack()

T.insert(tk.END, txt)
T.insert(tk.END, "Hello")
tk.mainloop()
