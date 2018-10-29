# import the ohbot module

from ohbot import ohbot

# Reset Ohbot

ohbot.reset()


# Switch the speech synthesizer to epseak
ohbot.setSynthesizer("espeak")

# Set the voice to english West Midlands accent medium speed.

ohbot.setVoice("-ven-wm+m1 -s150")

# Set eyes to red
ohbot.eyeColour(10,0,0)

ohbot.wait(0.5)

# Say something
ohbot.say("ha, ha, ha, haaaaaaaaaa", False)
ohbot.wait(0.5)
ohbot.say("Hello. I am Mary Webb. I have evil grooves from the dark side. Watch them ", False)
ohbot.wait(0.5)
ohbot.say("ha, ha, ha, haaaaaaaaaa", False)
# Wait a few seconds for the motors to move

ohbot.wait(2)

# Move head left to right
ohbot.move(ohbot.HEADTURN,5,1)
ohbot.wait(0.5)
ohbot.move(ohbot.HEADNOD,5,1)
ohbot.wait(0.5)
ohbot.eyeColour(0,10,0)
ohbot.wait(0.5)
ohbot.move(ohbot.EYETURN,5,1)
ohbot.wait(1)
ohbot.say("I will rise again. Take one sweet.", False)
ohbot.wait(8)
ohbot.say("ha, ha, ha, haaaaaaaaaa", False)
# close ohbot at the end.

ohbot.close()
