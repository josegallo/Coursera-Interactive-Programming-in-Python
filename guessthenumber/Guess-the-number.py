# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# global range
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    # ramdon 0 to 100   
    secret_number = random.randrange(0, num_range + 1)
    # print secret_number
    global num_guesses    
    if num_range == 100:
        num_guesses = 7
    if num_range == 1000:
        num_guesses = 10


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range 
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range 
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # converts it to an integer
    g = int (guess)
    # prints out a message
    print "Guess was", g
    # print secret_number
    if secret_number > g: 
        print "Higher!"       
    elif secret_number < g: 
        print "Lower!"       
    else: 
        print "Correct!"
        new_game()   
    global num_guesses
    num_guesses = num_guesses - 1
    if num_guesses > 0: 
            print "The remainder number of guesses is",num_guesses 
            print ""
    if num_guesses == 0:
            print "You roun out the number of guesses"
            print "The number was", secret_number
            print "Try again!"
            print ""
            new_game()  
    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
frame.add_input('Enter a guess', input_guess, 100)
button1 = frame.add_button('Range is [0,100)', range100, 100)
button2 = frame.add_button('Range is [0,1000)', range1000, 100)

# call new_game 
new_game()

frame.start()

# always remember to check your completed program against the grading rubric