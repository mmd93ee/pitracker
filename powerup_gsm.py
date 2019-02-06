#!/usr/bin/env python

# /etc/init.d/powerup_gsm.py

### BEGIN INIT INFO
# Provides:		powerup_gsm.py
# Required-Start:	
# Required-Stop:
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	Power Up GSM Module
# Description:		Enable GSM module to auto power up when pi is booted
### END INIT INFO


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

while True:
   GPIO.output(7, GPIO.LOW)
   time.sleep(4)
   GPIO.output(7, GPIO.HIGH)
   break

GPIO.cleanup()

