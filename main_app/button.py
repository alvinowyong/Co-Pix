from gpiozero import Button
import main

Question_Button = Button(2)
Start_Button = Button(3)

while 1:
    Start_Button.when_pressed = main.main_app()
