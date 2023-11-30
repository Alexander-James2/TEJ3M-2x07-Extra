# Alexander James
# Nov. 2023
# Combines a distance sensor and servo

import time
import board
import adafruit_hcsr04
import pwmio
from adafruit_motor import servo

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A0)
pwm = pwmio.PWMOut(board.A2, frequency=50)
ServoNumber1 = servo.Servo(pwm)

while True:
    try:
        if sonar.distance <= 20:
            ServoNumber1.angle = 180
        else:
            ServoNumber1.angle = 0
        time.sleep(0.1)
        print((sonar.distance,))

    except RuntimeError:  # Prevents crashing when an error occurs 
        print("Retrying!")
        time.sleep(0.1)
        