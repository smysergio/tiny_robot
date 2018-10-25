import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
from time import sleep  # Importing sleep from time library

m1_enable = 13
m2_enable = 17

motors = [6,5,22,27]

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering

GPIO.setup(m1_enable,GPIO.OUT)
GPIO.setup(m2_enable,GPIO.OUT)
GPIO.setup(motors[0],GPIO.OUT)
GPIO.setup(motors[1],GPIO.OUT)
GPIO.setup(motors[2],GPIO.OUT)
GPIO.setup(motors[3],GPIO.OUT)

GPIO.output(m1_enable,GPIO.HIGH)
GPIO.output(m2_enable,GPIO.HIGH)

GPIO.output(motors[0],GPIO.HIGH)
GPIO.output(motors[1],GPIO.LOW)
GPIO.output(motors[2],GPIO.HIGH)
GPIO.output(motors[3],GPIO.LOW)

time.sleep(5)

GPIO.output(motors[0],GPIO.LOW)
GPIO.output(motors[1],GPIO.LOW)
GPIO.output(motors[2],GPIO.LOW)
GPIO.output(motors[3],GPIO.LOW)

time.sleep(5)

GPIO.output(motors[0],GPIO.HIGH)
GPIO.output(motors[1],GPIO.LOW)
GPIO.output(motors[2],GPIO.HIGH)
GPIO.output(motors[3],GPIO.LOW)

time.sleep(5)

GPIO.output(motors[0],GPIO.LOW)
GPIO.output(motors[1],GPIO.LOW)
GPIO.output(motors[2],GPIO.LOW)
GPIO.output(motors[3],GPIO.LOW)