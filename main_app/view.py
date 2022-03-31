import tkinter as tk
from PIL import Image, ImageTk
import time
import os.path
import re
import math

DIVIDER = 12

def red_led():
    # Call red LED here
    print("red led")
    voice_indicate['text'] = "I am doubt"

def speech_to_text():
    clear_frame()
    render_waiting()
    print("start recording")
    # Call Speed to text function here
    time.sleep(5)
    clear_frame()
    # Recongized text goes here
    text = "The first little pig was very lazy. He abandon. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but the was somewhat lazy too and he built his house out of sticks."
    render_text(text)

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
                path = '../natural-language-processing/nouns/' + word + '.png'
                if os.path.exists(path):
                    image = Image.open(path)
                    resized_image= image.resize((44,44), Image.ANTIALIAS)
                    icon = ImageTk.PhotoImage(resized_image)
                    label = tk.Label(frame, image=icon)
                    label.image = icon
            label.pack(padx=5, pady=5)

root = tk.Tk()

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
