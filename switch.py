#load env
from dotenv import load_dotenv
load_dotenv()
import os

#### test without sending to Raspberry Pi #####

doorEnv = os.getenv("DOOR_ENV")

if doorEnv == "testing":
    print("Door Switch Triggered")
    exit(0)

###############################################

# import libs
import RPi.GPIO as GPIO           # import RPi.GPIO module  
import time

gpioPin = os.getenv("GPIO_PIN")

try:

    if not gpioPin:
        raise Exception("GPIO_PIN env is not set")
    
    GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
    GPIO.setup(gpioPin, GPIO.OUT) # set a port/pin as an output   

    GPIO.output(gpioPin, 1)       # set port/pin value to 1/GPIO.HIGH/True
    time.sleep(1)
    GPIO.output(gpioPin,0)

except KeyboardInterrupt:
    print("Keyboard Interrupt captured")
except Exception as e:
    print("Error: ", e)
finally:
    GPIO.cleanup() # proper clearning ofport so voltage is set back to default