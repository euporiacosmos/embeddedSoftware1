import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM) # BCM standard is made by a compny while BOARD standard is embed in RPi itself.
gpio.setup(4, gpio.IN, pull_up_down=gpio.PUD_UP) # pushButton
gpio.setup(18, gpio.OUT) # LED(red)

countButtonDown = 0
old_valPushButton = True

while(True):
    valPushButton = gpio.input(4)
    if not valPushButton:
        gpio.output(18, True) # LED OFF
        countButtonDown = countButtonDown + 1 # '+=' does not work
    
    old_valPushButton = valPushButton
    time.sleep(1)
    
    # print("Value of PushButton= ", valPushButton)
    print("CountButtonDown = ", countButtonDown)