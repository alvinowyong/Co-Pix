from tkinter import *
from tkinter import font
import tkinter as tk
from turtle import right
from PIL import Image, ImageTk
import time
import os.path
import re
import math
import led
from datetime import datetime
import s2t
import copixCamera
import upload
import random
from tkinter import messagebox

DIVIDER = 8

def red_led():
    # Call red LED here
    led.red_led()
    voice_indicate['text'] = "I'm in doubt"

def speech_to_text():
    led.off_leds()
    clear_frame()
    # Call Speed to text function here
    text = s2t.speech_to_text(2)

    # Recongized text goes here
    render_text(text)
    voice_indicate['text'] = "Complete"
    time.sleep(1)
    # Take a photo using camera module
    led.indicate()
    copixCamera.take_photo()

    # Fetch image from data folder
    # Upload image blob to Azure and call to Emotion Recognition API
    try:
        result = upload.emotion_recognition()

        # Log FER results into console
        print("[" + str(datetime.now().time()) + ": Log- FER Result]:", result)

        # Enable LED based on FER results
        if (result == 'happiness'):
            led.green_led()
        else:
            led.red_led()
    except Exception as e:
        print("[" + str(datetime.now().time()) + ": Error - Emotion Recognition]: Error occured")
        print(e)
        if (random.random()) > 0.5:
            led.green_led()
        else:
            led.red_led()
        

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
    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        led.off_leds()
        root.destroy()


    

root = tk.Tk()

root.title("Co-Pix")
root.protocol("WM_DELETE_WINDOW", on_closing)
# root.attributes('-fullscreen', True)

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

voice_indicate = tk.Label(content, text=" Home ", font=txt_btn, bg='white')

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
