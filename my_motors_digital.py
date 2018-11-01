import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time

print "Program Start"

m1_enable = 13
m2_enable = 17

MR = [27, 22]
ML = [6, 5]
# Left Motor: (1) motors[5] (2) motors[6] 
# Right Motor: (1) motors[27] (2) motors[22] 
# Forward (1=HIGH & 2=LOW) Reverse (1=LOW & 2=HIGH)

def control(motor,direction):
	print (motor+" "+direction)
	if (motor=="R"):
		m = [MR]
	elif (motor=="L"):
		m = [ML]
	elif (motor=="B"):
		m = [MR,ML]
	else:
		print "invalid motor"
	print m
	for x in m:
		if (direction=="forward"):
			GPIO.output(x[0],GPIO.HIGH)
			GPIO.output(x[1],GPIO.LOW)
		elif (direction=="reverse"):
			GPIO.output(x[0],GPIO.LOW)
			GPIO.output(x[1],GPIO.HIGH)
		elif (direction=="freewheel"):
			GPIO.output(x[0],GPIO.LOW)
			GPIO.output(x[1],GPIO.LOW)
		elif (direction=="block"):
			GPIO.output(x[0],GPIO.HIGH)
			GPIO.output(x[1],GPIO.HIGH)
		else:
			print "invalid direction"
	print "success"

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setwarnings(False)

GPIO.setup(m1_enable,GPIO.OUT)
GPIO.setup(m2_enable,GPIO.OUT)
GPIO.setup(MR[0],GPIO.OUT)
GPIO.setup(MR[1],GPIO.OUT)
GPIO.setup(ML[0],GPIO.OUT)
GPIO.setup(ML[1],GPIO.OUT)

GPIO.output(MR[0],GPIO.LOW)
GPIO.output(MR[1],GPIO.LOW)
GPIO.output(ML[0],GPIO.LOW)
GPIO.output(ML[1],GPIO.LOW)
GPIO.output(m1_enable,GPIO.LOW)
GPIO.output(m2_enable,GPIO.LOW)

print "Initialization complete"
time.sleep(5)


GPIO.output(m1_enable,GPIO.HIGH)
GPIO.output(m2_enable,GPIO.HIGH)

print "Starting Loop"
while 1:
	try:
		while(1):
			control("R","forward")
			time.sleep(5)
			control("L","forward")
			time.sleep(5)
			control("B","freewheel")
			time.sleep(5)
			control("B","reverse")
			time.sleep(5)
			control("R","block")
			control("L","freewheel")
			time.sleep(5)
			print "Loop Completed"
	
	finally:

		GPIO.setup(m1_enable,GPIO.LOW)
		GPIO.setup(m2_enable,GPIO.LOW)
		GPIO.setup(MR[0],GPIO.LOW)
		GPIO.setup(MR[1],GPIO.LOW)
		GPIO.setup(ML[0],GPIO.LOW)
		GPIO.setup(ML[1],GPIO.LOW)
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
