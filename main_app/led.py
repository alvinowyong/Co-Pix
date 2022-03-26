import RPi.GPIO as GPIO ## Import GPIO library
import time

def red_led():
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(7,True) ## Turn on GPIO pin 7
    

def green_led():
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(17, GPIO.OUT) ## Setup GPIO Pin 17 to OUT
    GPIO.output(17,True) ## Turn on GPIO pin 17
    
# def multi_color(input):
#     GPIO.setup(11, GPIO.OUT)
#     GPIO.output(11,1)
#     GPIO.setup(11, GPIO.OUT)
#     GPIO.output(13,1)
#     GPIO.setup(11, GPIO.OUT)
#     GPIO.output(15,1)
#     
#     if (input == happiness):
#         GPIO.output(11, 010)
# 
#     elif (input == neutural):
#         GPIO.output(13, 001)
# 
#     else:
#         GPIO.output(15, 100)
        
    
    
    
    