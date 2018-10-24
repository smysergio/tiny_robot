import RPi.GPIO as GPIO
import time

# test push

led_red = 20
led_yellow = 16
led_green = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.setup(led_red,GPIO.OUT)
#PIO.setup(led_yellow,GPIO.OUT)
GPIO.setup(led_green,GPIO.OUT)
print "LED on"
#GPIO.output(led_red,GPIO.HIGH)
#GPIO.output(led_yellow,GPIO.HIGH)
GPIO.output(led_green,GPIO.HIGH)
time.sleep(1)
print "LED off"
#GPIO.output(led_red,GPIO.LOW)
#GPIO.output(led_yellow,GPIO.LOW)
GPIO.output(led_green,GPIO.LOW)