import Adafruit_BBIO.GPIO as GPIO    # importing adafruit library
import time                          # importing time library for delay

M1= "P8_8"                           # declaring motor pins
M2= "P8_10"
M3= "P8_12"
M4= "P8_14" 

GPIO.setup(M1, GPIO.OUT)             # setting motor pins as output
GPIO.setup(M2, GPIO.OUT)
GPIO.setup(M3, GPIO.OUT)
GPIO.setup(M4, GPIO.OUT)

while True:                          # to run continously
	GPIO.output(M1, GPIO.HIGH)   # to run forward
        GPIO.output(M2, GPIO.LOW)    
        time.sleep(5)                # to run for 5 seconds
        GPIO.output(M1, GPIO.LOW)    # to stop motor
        GPIO.output(M2, GPIO.LOW)
        time.sleep(2)                # to wait for 2 seconds
        GPIO.output(M1, GPIO.LOW)    # to run backward
        GPIO.output(M2, GPIO.HIGH)
	time.sleep(5)                # to run for 5 seconds
