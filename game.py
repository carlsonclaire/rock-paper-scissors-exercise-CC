
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
if (c == 'rock') and (x == 'paper'):
    print('you win')
if (c == 'rock') and (x == 'scissors'):
    print('you lose')
if (c == 'rock') and (x == 'rock'):
      print('tie, try again')
if (c == 'paper') and (x == 'paper'):
    print('you tie, try again')
if (c == 'paper') and (x == 'scissors'):
    print('you win')
if (c == 'paper') and (x == 'rock'):
    print('you lose')
if (c == 'scissors') and (x == 'paper'):
    print('you win')
if (c == 'scissors') and (x == 'scissors'):
    print('tie, try again')
if (c == 'scissors') and (x == 'rock'):
    print('you win')
# DISPLAY THE FINAL RESULTS
