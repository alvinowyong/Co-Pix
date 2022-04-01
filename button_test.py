from gpiozero import Button
import main

Question_Button = Button(2)
Start_Button = Button(3)


def press():
    print("press me")
    return 1


while 1:
    Start_Button.when_pressed = press()
