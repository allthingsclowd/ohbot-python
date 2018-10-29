#!/usr/bin/python
"""Summary: Quick script for Halloween Skeleton Prank for Kids

Author: Graham Land
Date: 29/10/18
Twitter: @allthingsclowd
Github: https://github.com/allthingscloud
Blog: https://allthingscloud.eu
"""

import RPi.GPIO as GPIO
import time

# import the ohbot module

from ohbot import ohbot


def get_steven_to_talk():
    """Run the Ohbot routine
    Returns:
        Boolean True or False depending on whether run successfully or not
    """
    
    try:
        # Reset Ohbot

        ohbot.reset()

        # Switch the speech synthesizer to epseak
        ohbot.setSynthesizer("espeak")

        # Set the voice to english West Midlands accent medium speed.

        ohbot.setVoice("-ven+f2 -s130")

        # Set eyes to red
        ohbot.eyeColour(10,0,0)

        ohbot.wait(0.5)

        # Say something
        ohbot.say("Good Evening",True, False, False,0)
        ohbot.wait(0.5)
        #ohbot.say("Who have we got here",True, False, False,0)
        #ohbot.wait(0.5)
        ohbot.say("I'm the late great Mary Webb ",True, False, False,0)
        ohbot.wait(0.5)
        ohbot.say("I love children ",True, False, False,0)
        ohbot.wait(0.5)
        ohbot.say("For supper",True, False, False,0)
        ohbot.wait(0.5)
        #ohbot.say("Woooahhhh woooahhha",True, False, False,0)
        #ohbot.wait(0.5)
        # Wait a few seconds for the motors to move

        ohbot.wait(2)

        # Move head left to right
        ohbot.move(ohbot.HEADTURN,4,1)
        ohbot.wait(1)
        ohbot.move(ohbot.HEADTURN,6,1)
        ohbot.wait(1)
        ohbot.move(ohbot.HEADTURN,5,1)
        ohbot.wait(1)
        ohbot.eyeColour(0,10,0)
        ohbot.wait(0.5)
        ohbot.move(ohbot.HEADNOD,7,1)
        ohbot.wait(1)
        ohbot.move(ohbot.HEADNOD,1,1)
        ohbot.wait(1)
        ohbot.move(ohbot.EYETURN,9,1)
        ohbot.wait(1)
        ohbot.move(ohbot.EYETURN,1,1)
        ohbot.wait(1)
        ohbot.move(ohbot.EYETURN,5,1)
        ohbot.wait(1)
        ohbot.say("Take one sweet.",True, False, False,0)
        ohbot.wait(0.5)
        ohbot.say("At your own risk",True, False, False,0)
        ohbot.wait(0.5)
        ohbot.say("Don't forget to brush your teeth",True, False, False,0)
        ohbot.wait(0.55)
        ohbot.say("Happy Halloween",True, False, False,0)
        ohbot.wait(0.55)
        ohbot.reset()
        # close ohbot at the end.
        ohbot.wait(5)
        ohbot.close()
        ohbot.wait(5)
        return True
    except:
        return False


def main():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
    GPIO.setup(13, GPIO.IN)         #Read output from BUTTON sensor
    BUSY=False

    while True:
        
        PIR=GPIO.input(11)
        BUTTON=GPIO.input(13)
        if (PIR==1 or BUTTON==1) and not BUSY:                #When output from motion sensor is High
            BUSY=True
            get_steven_to_talk()
            BUSY=False


if __name__ == "__main__":
    main()