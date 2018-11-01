import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time


m1_enable = 13
MR = [6, 5]

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setwarnings(False)

GPIO.setup(m1_enable,GPIO.OUT)
GPIO.setup(MR[0],GPIO.OUT)
GPIO.setup(MR[1],GPIO.OUT)

pwm_mr1 = GPIO.PWM(MR[0], 100)    # Created a PWM object
pwm_mr1.start(0)                    # Started PWM at 0% duty cycle
pwm_mr2 = GPIO.PWM(MR[0], 100)    # Created a PWM object
pwm_mr2.start(0)                    # Started PWM at 0% duty cycle
GPIO.output(m1_enable,GPIO.LOW)


print "Initialization complete"
time.sleep(1)

GPIO.output(m1_enable,GPIO.HIGH)

print "Starting Loop"
while 1:
	try:
		while(1):
			for x in range(70,101):
				print x
				pwm_mr1.ChangeDutyCycle(100) # Change duty cycle
				time.sleep(3)

	
	finally:

		GPIO.setup(m1_enable,GPIO.LOW)
		pwm_mr1.stop()      # Stop the PWM
		pwm_mr2.stop()      # Stop the PWM
		GPIO.cleanup()  # Make all the output pins LOW
		print "Clean Exit!"
