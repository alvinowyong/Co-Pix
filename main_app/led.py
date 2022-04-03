import RPi.GPIO as GPIO ## Import GPIO library
import time

"""
Utilise GPIO pins to control LED indicators based on results of FER.
"""

# Utilise Broaddcom SOC channel for addressing pins
GPIO.setmode(GPIO.BCM)
# Disable runtime warning
GPIO.setwarnings(False)

# Set GPIO pins to OUTPUT mode
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

def red_led():
    # Turn on GPIO pin 27
    GPIO.output(27,GPIO.HIGH)
    
def green_led():
    # Turn on GPIO pin 17
    GPIO.output(17,GPIO.HIGH)
    
def off_leds():
    # Turn of both GPIO pins
    GPIO.output(27,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    
def indicate():
    # Turn on GPIO pin 17
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(27,GPIO.LOW)
    
def error():
    # Turn on GPIO pin 27
    GPIO.output(27,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(27,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(27,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(27,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(27,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(27,GPIO.LOW)
    
def success():
    # Turn on GPIO pin 27
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)   
    