import RPi.GPIO as GPIO
import time
import os
import glob
#GPIO SETUP
GPIO.setmode(GPIO.BCM)
Button = 21
n = 1
GPIO.setup(Button,GPIO.IN)
#loop
print("Program Running")
while 1 == 1:
  if GPIO.input(Button) == False:
    print("Button Pressed")
    
    now = time.strftime("Date%m-%d-%yTime%H-%M-%S")
   
    command = "bash oscmds.sh " +  str(now)
    
    
    os.system(command)
    #diagnostics
    print("Filename:", now)
    
  
    
    print("Email")
    emailcommand = 'python3 IOTNOTIFY2.py "Someone is at the door"' + ' "photos/' + now + '.jpg"'
    os.system(emailcommand) #running the Email script with:
    
    print("Done Process")
    
    print("")
    print("")
