# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    
    # This last one is just for testing in case of error
    else:
        print "Houston we have a problem with the numbers"
    
def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    
    # This last one is just for testing in case of error
    else:
        print 'Houston we have a problem with the names'


def rpsls(name):
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
 
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)
    
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5


    # convert comp_number to name using number_to_name
    computer_guess = number_to_name(comp_number)

    
    # use if/elif/else to determine winner
    # print results
    if difference == 0:
        print "Player chooses " + name
        print "Computer chooses " + computer_guess
        print 'Player and Computer tie.'
        print " "
        
    elif difference == 1 or difference == 2:
        print "Player chooses " + name
        print "Computer chooses " + computer_guess
        print 'Player wins!'
        print " "
        
    elif difference == 3 or difference == 4:
        print "Player chooses " + name
        print "Computer chooses " + computer_guess
        print 'Computer wins!'
        print " "
        
    # This last one is just for testing in case of error
    else:
        print 'Houston... are you there?!?'



# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


