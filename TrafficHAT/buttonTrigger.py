#!/usr/bin/env python
import RPi.GPIO as IO
from time import sleep
IO.setmode(IO.BCM)

RED = 24
YELLOW = 23
GREEN = 22
BUTTON = 25
BUZZER = 5

outputs = [RED, YELLOW, GREEN, BUZZER]
for output in outputs:
    IO.setup(output,IO.OUT)

IO.setup(BUTTON,IO.IN, pull_up_down=IO.PUD_UP)

currentLED = 0

try:
    while True:
    	if currentLED == 0:
	        IO.output(GREEN, 1)
	        IO.output(YELLOW, 0)
	        IO.output(RED, 0)    	
    	elif currentLED == 1:
	        IO.output(GREEN, 0)
	        IO.output(YELLOW, 1)
	        IO.output(RED, 0)    	
    	elif currentLED == 2:
	        IO.output(GREEN, 0)
	        IO.output(YELLOW, 0)
	        IO.output(RED, 1)    
        while(IO.input(BUTTON) == 1):
        	pass
        if currentLED == 2:
        	currentLED = 0
        else:
        	currentLED = currentLED + 1
        i = 0 
        while(i<2):
            #Turn Buzzer On
            IO.output(BUZZER,1)
            #Wait 0.01 Seconds
            sleep(0.1)
            #Turn Buzzer LED Off
            IO.output(BUZZER,0)
            #Wait 0.01 Seconds
            sleep(0.05)
            #Add 1 to the count
            i = i+1

        sleep(0.1)

except KeyboardInterrupt:
    IO.cleanup()

except:
    print "Error!"
    raise
