from tkinter import *
from tkinter import font
import tkinter as tk
from turtle import right
from PIL import Image, ImageTk
import time
import os.path
import re
import math

DIVIDER = 10

def red_led():
    # Call red LED here
    print("red led")
    voice_indicate['text'] = "Doubt"

def speech_to_text():
    voice_indicate['text'] = "Listening"
    clear_frame()
    print("start recording")
    # Call Speed to text function here
    time.sleep(2)
    clear_frame()
    # Recongized text goes here
    # text = "The first little pig was very lazy."

    text = "The first little pig was very lazy. He abandon. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but the was somewhat lazy too and he built his house out of sticks."
    
    # text = "The first little pig was very lazy. He abandon. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but the was somewhat lazy too and he built his house out of sticks., The first little pig was very lazy. He abandon. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but the was somewhat lazy too and he built his house out of sticks. "
    render_text(text)
    voice_indicate['text'] = "Complete"

def clear_frame():
    for widget in fr_text.winfo_children():
        widget.destroy()
    fr_text.pack_forget()

def render_text(text):
    words = text.split(" ")
    count = math.ceil(len(words)/DIVIDER) * 2

    canvas = tk.Canvas(fr_text)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    vsb = tk.Scrollbar(fr_text, orient="vertical", command=canvas.yview)
    vsb.pack(side=RIGHT, fill=Y)
    canvas.config(yscrollcommand=vsb.set)

    frame_words = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_words, anchor='nw')

    for i in range(count):
        frame_words.columnconfigure(i, minsize=screen_width/DIVIDER)
        frame_words.rowconfigure(i)
        
        for j in range(0, DIVIDER):
            frame = tk.Frame(
                master=frame_words,
                relief=tk.RAISED,
            )
            frame.grid(row=i, column=j, sticky=(N, S, E, W))
            index = int(i/2) * DIVIDER + j
            if(index >= len(words)):
                continue
            word = words[index].capitalize()
            if(i % 2 == 0):
                label = tk.Label(frame, text=words[index])
                label.configure(font=txt_font)
            else:
                word = re.sub(r'[^a-zA-Z]', '', word)
                path = '../natural-language-processing/nouns/' + word + '.png'
                if os.path.exists(path):
                    image = Image.open(path)
                    resized_image= image.resize((44,44), Image.ANTIALIAS)
                    icon = ImageTk.PhotoImage(resized_image)
                    label = tk.Label(frame, image=icon)
                    label.image = icon
            label.pack(padx=5, pady=2)
    frame_words.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    

root = tk.Tk()
root.title("Co-Pix")
root.attributes('-fullscreen', True)

content = tk.Frame(root)
fr_text = tk.Frame(content, relief="ridge", bg="white")

#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Use this to view all fonts
# print(font.families())

# Font Size
txt_font = ("OpenDyslexic 3", 24)
txt_btn = ("OpenDyslexic 3", 26)

# Creating a photoimage object to use image
doubt_image = Image.open('./img/doubt.png')
doubt_resize= doubt_image.resize((80,80), Image.ANTIALIAS)
doubt_icon = ImageTk.PhotoImage(doubt_resize)

record_image = Image.open('./img/record.png')
record_resize= record_image.resize((60,60), Image.ANTIALIAS)
record_icon = ImageTk.PhotoImage(record_resize)

btn_doubt = tk.Button(content, text="Doubt", command=red_led, height=150, compound=TOP,
                      image=doubt_icon, bd=0, bg='#FFF380', font=txt_btn)

voice_indicate = tk.Label(content, text="Listening", font=txt_btn, bg='white')

btn_record = tk.Button(content, text="Record", command=speech_to_text, height=150, compound=TOP,
                       image=record_icon, bd=0, bg='#FFF380', font=txt_btn)

content.grid(column=0, row=0, sticky=(N, S, E, W))
fr_text.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
btn_doubt.grid(column=0, row=3, sticky=(N, S, E, W))
voice_indicate.grid(column=1, row=3, sticky=(N, S, E, W))
btn_record.grid(column=2, row=3, sticky=(N, S, E, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.rowconfigure(1, weight=1)

root.mainloop()
