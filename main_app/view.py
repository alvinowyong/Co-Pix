from pickle import TRUE
from tkinter import font
import tkinter as tk
from turtle import color
from PIL import Image, ImageTk
import time
import os.path
import re
import math
import led
import s2t
import camera
import upload

DIVIDER = 12

def red_led():
    # Call red LED here
    led.red_led()
    voice_indicate['text'] = "I'm in doubt"

def speech_to_text():
    led.off_leds()
    clear_frame()
    render_waiting()
    print("start recording")
    # Call Speed to text function here
    text = s2t.speech_to_text(2)
    time.sleep(1)
    clear_frame()
    # Recongized text goes here
    render_text(text)
    time.sleep(7)
    # Take a photo using camera module
    camera.take_photo()

    # Fetch image from data folder
    # Upload image blob to Azure and call to Emotion Recognition API
    result = upload.emotion_recognition()

    # Log FER results into console
    print("[Log- FER Result]:", result)

    # Enable LED based on FER results
    if (result == 'happiness'):
        led.green_led()
    else:
        led.red_led()

def render_waiting():
    txt_label = tk.Label(fr_text, text="Listening")
    txt_label.grid(row=0, column=0, sticky="wesn", padx=15, pady=15)

def clear_frame():
    for widget in fr_text.winfo_children():
        widget.destroy()
    fr_text.pack_forget()

def render_text(text):
    words = text.split(" ")
    count = math.ceil(len(words)/DIVIDER) * 2
    for i in range(count):
        fr_text.columnconfigure(i, weight=1)
        fr_text.rowconfigure(i, weight=1)
        
        for j in range(0, DIVIDER):
            frame = tk.Frame(
                master=fr_text,
                relief=tk.RAISED,
            )
            frame.grid(row=i, column=j)
            index = int(i/2) * DIVIDER + j
            if(index >= len(words)):
                continue
            word = words[index].capitalize()

            if(i % 2 == 0):
                label = tk.Label(frame, text=words[index])
                label.configure(font=txt_font)
            else:
                word = re.sub(r'[^a-zA-Z]', '', word)
                path = '../natural-language-processing/nouns32/' + word + '.png'
                if os.path.exists(path):
                    image = Image.open(path)
                    resized_image= image.resize((44,44), Image.ANTIALIAS)
                    icon = ImageTk.PhotoImage(resized_image)
                    label = tk.Label(frame, image=icon)
                    label.image = icon
            label.pack(padx=5, pady=5)

root = tk.Tk()
root.title("Co-Pix")
root.iconbitmap("copix_small.ico")
window = tk.Frame(root)

#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window = tk.Frame(root, width=screen_width, height=screen_height, bg="blue")
root.attributes('-fullscreen', True)

window.rowconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

txt_font = ("Times New Roman", 24)

fr_text = tk.Frame(window, width=screen_width, height=80, bg="red")

fr_buttons = tk.Frame(window, width=screen_width, height=screen_height-80, bg="green")
# Creating a photoimage object to use image
doubt_image = Image.open('./img/doubt.png')
doubt_icon = ImageTk.PhotoImage(doubt_image)
record_image = Image.open('./img/record.png')
record_icon = ImageTk.PhotoImage(record_image)

btn_doubt = tk.Button(window, text="Doubt", command=red_led,
                      image=doubt_icon, compound=tk.TOP, padx=15, pady=5, bd=0, bg='#FFF380')
voice_indicate = tk.Label(window, text="Listening")
btn_record = tk.Button(window, text="Record", command=speech_to_text,
                       image=record_icon, compound=tk.TOP, padx=15, pady=5, bd=0, bg='#FFF380')

btn_doubt.grid(row=1, column=0, padx=15, pady=15, sticky="w")
voice_indicate.grid(row=1, column=1, padx=15, pady=15, sticky='we')
btn_record.grid(row=1, column=2, padx=15, pady=15, sticky="e")

txt_label = tk.Label(fr_text, text="Listening")
txt_label.grid(row=0, column=0, sticky="wesn", padx=15, pady=15)

fr_text.grid(row=0, column=0, columnspan=3, sticky="ns")
# fr_buttons.grid(row=1, column=0, sticky="s")

window.pack(fill=tk.BOTH)

root.mainloop()
