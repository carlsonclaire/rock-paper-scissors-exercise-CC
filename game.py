
#IMPORTS
import random


# WHAT WE'RE TRYING TO DO
print('Rock, Paper, Scissors, Shoot!')

# ASK FOR A USER INPUT
# source: add URL here
x=input("Please choose 'rock', 'paper', 'scissors'")
print(x)

# VALIDATE THE USER INPUT
# Reminder to ask Prof why we need to print "valid"
if (x == 'rock') or (x == 'paper') or (x == 'scissors'):
    print('valid')
else:
    print('OOPS, INVALID, PLEASE TRY AGAIN')
    exit()
print("USER CHOSE: ",x)

# GENERATE A COMPUTER CHOICE
# SOURCE: STACK OVERFLOW
valid_options = ['rock','paper','scissors']
c = random.choice(valid_options)
print("COMPUTER CHOSE:",c)

# DETERMINE THE WINNER


# DISPLAY THE FINAL RESULTS
