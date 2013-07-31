# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100

# helper function to initialize the game
# def init():

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = random.randrange(0,100)
    return num_range


def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = random.randrange(0,1000)
    return num_range

    
def get_input(guess):
    # main game logic goes here
    print "GUESS"

    

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

# start frame
frame.start()

# always remember to check your completed program against the grading rubric
