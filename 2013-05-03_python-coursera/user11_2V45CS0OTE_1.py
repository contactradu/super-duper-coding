# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100

# helper function to initialize the game
def init()

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts

def range1000():
    # button that changes range to range [0,1000) and restarts
    
def get_input(guess):
    # main game logic goes here	

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range100, 200)
f.add_input("Enter a guess", get_input, 200)

# start frame
init()

# always remember to check your completed program against the grading rubric
