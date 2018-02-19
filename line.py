import sys, rospy
import RPi.GPIO as GPIO

speed = 100

def start(p1, p2, p3, p4):
    p1.ChangeDutyCycle(speed)
    p2.ChangeDutyCycle(0)
    p3.ChangeDutyCycle(speed)
    p4.ChangeDutyCycle(0)

if __name__=="__main__":
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
    p1 = GPIO.PWM(35, 10)
    p2 = GPIO.PWM(36, 10)
    p3 = GPIO.PWM(37, 10)
    p4 = GPIO.PWM(38, 10)
    #Start PWM
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)

    rospy.init_node('teleop_twist_keyboard')
    try:
        while(True):
            start(p1, p2, p3, p4)

    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()