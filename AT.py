#!/usr/bin/python

import RPi.GPIO as GPIO
import serial
import time,sys
import datetime

try:
	ser = serial.Serial("/dev/ttyUSB2",115200)
	ser.flushInput()
	print("Setup ok")
except:
	print("ERROR")

power_key = 4
command_input = ''
rec_buff = ''

kadal = 0
print("Mencoba")
while True:
	# print("Loop")
	if kadal==0:
		command_input = "AT+CMGF=1"	
		ser.write((command_input+  '\r\n' ).encode())
		time.sleep(0.1)
		if ser.inWaiting():
			time.sleep(0.01)
			rec_buff = ser.read(ser.inWaiting())
		if rec_buff != '':
			print(rec_buff.decode())
			rec_buff = ''
			kadal = 1

	if kadal==1:
		msg = ("HI RARA AKU MODEM") 
		print ("Sending SMS with status info:")
		time.sleep(3)
		ser.write(str.encode(msg+chr(26)))
		time.sleep(0.1)
		if ser.inWaiting():
			time.sleep(0.01)
			rec_buff = ser.read(ser.inWaiting())
		if rec_buff != '':
			print(rec_buff.decode())
			rec_buff = ''
			print("message sent…")
			kadal = 2
			
	if kadal==2:
	    command_signal="AT+CSQ"
	    time.sleep(3)
	    print ("Signal info")
	    hasil=ser.write((command_signal+ '\r\n').encode())
	    time.sleep(0.1)
	    if ser.inWaiting():
	        time.sleep(0.01)
	        rec_buff = ser.read(ser.inWaiting())
	    if rec_buff != '':
	        print(rec_buff.decode())
	        rec_buff = ''
	        kadal = 3
	        
	        
    if kadal==3:
        url="http://navier-development.azurewebsites.net/api/dronelist/drone/add-data"
        
