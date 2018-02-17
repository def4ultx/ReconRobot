import sys
import RPi.GPIO as GPIO

speed = 28.5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#OUTPUT
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
#INPUT
GPIO.setup(29, GPIO.IN)
GPIO.setup(31, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
#PWM
p1 = GPIO.PWM(35, 50)
p2 = GPIO.PWM(36, 50)
p3 = GPIO.PWM(37, 50)
p4 = GPIO.PWM(38, 50)
#Start PWM
p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)

def start():
    p1.ChangeDutyCycle(speed)
    p2.ChangeDutyCycle(0)
    p3.ChangeDutyCycle(speed)
    p4.ChangeDutyCycle(0)

def forward():#20
    p1.ChangeDutyCycle(speed)
    p2.ChangeDutyCycle(0)
    p3.ChangeDutyCycle(speed)
    p4.ChangeDutyCycle(0)

def left():
    p1.ChangeDutyCycle(speed)
    p2.ChangeDutyCycle(0)
    p3.ChangeDutyCycle(0)
    p4.ChangeDutyCycle(speed)

def right():
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(speed)
    p3.ChangeDutyCycle(speed)
    p4.ChangeDutyCycle(0)

def stop():
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
    p3.ChangeDutyCycle(0)
    p4.ChangeDutyCycle(0)

def backward():
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(speed)
    p3.ChangeDutyCycle(0)
    p4.ChangeDutyCycle(speed)

def clean():
    p1.stop()
    p2.stop()
    p3.stop()
    p4.stop()

try:
    start()

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()