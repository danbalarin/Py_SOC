#!/usr/bin/python
import RPi.GPIO as GPIO
print "Verze GPIO knihovny"
print GPIO.VERSION

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(7,True) ## Turn on GPIO pin 7
print "Zapnuto"