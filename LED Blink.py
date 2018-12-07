import Adafruit_BBIO.GPIO as GPIO    # importing adafruit library
import time                          # importing time library for delay

led = "P8_10"                        # declaring led to pin 10 in P8
GPIO.setup(led, GPIO.OUT)            # setting led pin as output

While True:                          # to run continously
	GPIO.output(led, GPIO.HIGH)  # giving high signal to led
	time.sleep(0.5)	             # high signal for 0.5 seconds(500ms)
	GPIO.output(led, GPIO.LOW)   # giving low signal to led
	time.sleep(0.5)              # low signal for 0.5 seconds(500ms)
