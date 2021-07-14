
# IMPORTS
import random
import os
from dotenv import load_dotenv
load_dotenv()
z = os.getenv("PLAYER_NAME")
print(z)
print(exit)

# PLAY THE GAME
print('Hello and welcome to a game we like to call Rock, Paper, Scissors, Shoot!')

# ASK FOR A USER INPUT
# SOURCE: https://docs.python.org/3/library/functions.html#input
x=input("Please choose and type in 'Rock', 'Paper', 'Scissors'")
print(x)

# VALIDATE THE USER INPUT
if (x == 'Rock') or (x == 'Paper') or (x == 'Scissors'):
    print('One moment please while we make your move.')
else:
    print('Hmm, that does not look like a valid input, try again -- capitalization matters!')
    exit()
print("USER CHOSE:",x)

# GENERATE A COMPUTER CHOICE
# SOURCE: IMPORT FROM STACK OVERFLOW, https://docs.python.org/3/library/random.html
valid_options = ['Rock','Paper','Scissors']
c = random.choice(valid_options)
print("COMPUTER CHOSE:",c)

# DETERMINE THE WINNER AND DISPLAY THE FINAL RESULTS
# SOURCE: IMPROVEMENTS TO CODE THANKS TO PEER SHARING DURING 07/13 PYTHON AND PROGRAMMING FUNDAMENTAL CLASS FOR SHARING APPROACH
if (c == x):
    print('Tie, play again.')
elif c == 'Rock' and x == 'Paper':
    print('You win! Congrats.')
elif (c == 'Rock') and (x == 'Scissors'):
    print('Sorry, you lose.')
elif (c == 'Paper') and (x == 'Scissors'):
    print('You win! Congrats.')
elif (c == 'Paper') and (x == 'Rock'):
    print('Sorry, you lose.')
elif (c == 'Scissors') and (x == 'Paper'):
    print('You win! Congrats.')
elif (c == 'Scissors') and (x == 'Rock'):
    print('You win! Congrats.')
print('Win, lose, or tie, we thank you for playing!')
