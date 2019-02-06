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
import serial
import time

ser = serial.Serial("/dev/ttyAMA0",115200)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

# Start the hat
while True:
   GPIO.output(7, GPIO.LOW)
   time.sleep(4)
   GPIO.output(7, GPIO.HIGH)
   break

# Power up the GPS component of the hat
write_buffer = ["AT+CGNSPWR=1\r\n", "AT+CGNSSEQ=\"RMS\"\r\n", "AT+CGNSINF\r\n", "AT+CGNSURC=2\r\n", "AT+CGNSTST=1\r\n"]
ser.write(write_buffer[0])
ser.flushInput()

# Finish up...
GPIO.cleanup()

