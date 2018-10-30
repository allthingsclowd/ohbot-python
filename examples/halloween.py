#!/usr/bin/python
"""Summary: Quick script for Halloween Skeleton Prank for Kids

Author: Graham Land
Date: 29/10/18
Twitter: @allthingsclowd
Github: https://github.com/allthingscloud
Blog: https://allthingscloud.eu
"""

import RPi.GPIO as GPIO
from subprocess import call
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

def play_fart():
    print("FARTING")
    call(["aplay","/ohbot-python/examples/fart-04.wav"])
    return

def main():

    ohbot.reset()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)         #Read output from PIR motion sensor
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)         #Read output from BUTTON sensor

    while True:

        PIR=GPIO.input(8)
        BUTTON=GPIO.input(10)
        print(PIR)
        print(BUTTON)
        if (PIR==1):                #When output from motion sensor is High
            get_steven_to_talk()
            print("PIR")
            time.sleep(0.1)
        if (BUTTON==1):
            play_fart()
            time.sleep(0.1)
        time.sleep(0.1)

if __name__ == "__main__":
    main()