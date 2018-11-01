import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time


print "Program Start"

m1_enable = 13
m2_enable = 17

MR = [27, 22]
ML = [6, 5]
pwm_freq = 100
pwm_mr = [GPIO.PWM, GPIO.PWM]
pwm_ml = [GPIO.PWM, GPIO.PWM]

def control(motor,direction,speed = 100):
	print (motor+" "+direction)
	if (motor=="R"):
		m = [pwm_mr]
	elif (motor=="L"):
		m = [pwm_ml]
	elif (motor=="B"):
		m = [pwm_mr,pwm_ml]
	else:
		print "invalid motor"
	print m
	for x in m:
		if (direction=="forward"):
			x[0].ChangeDutyCycle(speed) # Change duty cycle
			x[1].ChangeDutyCycle(0) # Change duty cycle
		elif (direction=="reverse"):
			x[0].ChangeDutyCycle(0) # Change duty cycle
			x[1].ChangeDutyCycle(speed) # Change duty cycle
		elif (direction=="freewheel"):
			x[0].ChangeDutyCycle(0) # Change duty cycle
			x[1].ChangeDutyCycle(0) # Change duty cycle
		elif (direction=="block"):
			x[0].ChangeDutyCycle(100) # Change duty cycle
			x[1].ChangeDutyCycle(100) # Change duty cycle
		else:
			print "invalid direction"
	print "success"


# Left Motor: (1) motors[5] (2) motors[6] 
# Right Motor: (1) motors[27] (2) motors[22] 
# Forward (1=HIGH & 2=LOW) Reverse (1=LOW & 2=HIGH)

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setwarnings(False)

GPIO.setup(m1_enable,GPIO.OUT)
GPIO.setup(m2_enable,GPIO.OUT)
GPIO.setup(MR[0],GPIO.OUT)
GPIO.setup(MR[1],GPIO.OUT)
GPIO.setup(ML[0],GPIO.OUT)
GPIO.setup(ML[1],GPIO.OUT)


pwm_mr = [GPIO.PWM(MR[0], pwm_freq), GPIO.PWM(MR[1], pwm_freq)]   # Created a PWM object
pwm_mr[0].start(0)                    # Started PWM at 0% duty cycle
pwm_mr[1].start(0)                    # Started PWM at 0% duty cycle

pwm_ml = [GPIO.PWM(ML[0], pwm_freq), GPIO.PWM(ML[1], pwm_freq)]   # Created a PWM object
pwm_ml[0].start(0)                    # Started PWM at 0% duty cycle
pwm_ml[1].start(0)                    # Started PWM at 0% duty cycle

GPIO.output(m1_enable,GPIO.LOW)
GPIO.output(m2_enable,GPIO.LOW)


print "Initialization complete"
time.sleep(2)


GPIO.output(m1_enable,GPIO.HIGH)
GPIO.output(m2_enable,GPIO.HIGH)

print "Starting Loop"
while 1:
	try:
		while(1):
			control("R","forward")
			time.sleep(5)
			control("L","forward",40)
			time.sleep(5)
			control("B","freewheel")
			time.sleep(5)
			control("B","reverse",50)
			time.sleep(5)
			control("R","block")
			control("L","freewheel")
			time.sleep(5)
			print "Loop Completed"
	
	finally:

		GPIO.setup(m1_enable,GPIO.LOW)
		GPIO.setup(m2_enable,GPIO.LOW)
		pwm_mr[0].stop()      # Stop the PWM
		pwm_mr[1].stop()      # Stop the PWM
		pwm_ml[0].stop()      # Stop the PWM
		pwm_ml[1].stop()      # Stop the PWM
		GPIO.cleanup()
		print "Clean Exit!"


# GPIO.output(m1_enable,GPIO.HIGH)
# GPIO.output(m2_enable,GPIO.HIGH)

# GPIO.output(motors[0],GPIO.HIGH)
# GPIO.output(motors[1],GPIO.LOW)
# GPIO.output(motors[2],GPIO.HIGH)
# GPIO.output(motors[3],GPIO.LOW)

# time.sleep(5)

# GPIO.output(motors[0],GPIO.LOW)
# GPIO.output(motors[1],GPIO.LOW)
# GPIO.output(motors[2],GPIO.LOW)
# GPIO.output(motors[3],GPIO.LOW)

# time.sleep(5)

# GPIO.output(motors[0],GPIO.HIGH)
# GPIO.output(motors[1],GPIO.LOW)
# GPIO.output(motors[2],GPIO.HIGH)
# GPIO.output(motors[3],GPIO.LOW)

# time.sleep(5)

# GPIO.output(motors[0],GPIO.LOW)
# GPIO.output(motors[1],GPIO.LOW)
# GPIO.output(motors[2],GPIO.LOW)
# GPIO.output(motors[3],GPIO.LOW)
