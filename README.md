# Rock Paper Scissors Exercise
Example materials and support from Professor Rosetti were leveraged heavily in the creation of this game.
+ Source: Prof. Rosetti "My First Python App" ReadMe example
+ Source: https://github.com/ma-shamshiri/Pacman-Game#readme found from a listing of "GitHub" ReadME template examples

This is a simple game that you can install to play rock, paper, scissors against a computer opponent.

# Prerequisites
+ Anaconda 3.7
+ Python 3.7+
+ Pip

# Project files description
+ game.py - where all of the game code and logic resides
+ requirements.txt - where you can see the package that is required for this game
+ .env - where credentials will be input and passed through to the game
+ .gitignore - where you can see which files will not be uploaded to GitHub


# Install the repository
Fork this [remote repository](https://github.com/carlsonclaire/rock-paper-scissors-exercise-CC) under your own control, then "clone" or download your remote copy onto your local computer.

Navigate to your game from the command line based on where it's stored on your computer and the title you've given your game. For example:

```sh
cd rock-paper-scissors-exercise
```

# Install the dotenv package
# Source: Professor Rosetti in-class and GitHub examples
Before you run the Python script, you'll need to install the .env files. This will allow you to enter player credentials.

```import os
from dotenv import load_dotenv
load_dotenv()
z = os.getenv("PLAYER_NAME")
print(z)
print(exit)
```

```Then, use Anaconda to create and activate a new virtual environment:

```sh
conda create -n my-first-env python=3.8
conda activate my-first-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username (then make sure to SAVE the ".env" file afterwards):

    USER_NAME="Your name"

# Playing the game
Now, start playing your game!
```py
python game.py

# Game play
The user will first be asked to input their choice between rock, paper or scissors
```x=input("Please choose and type in 'Rock', 'Paper', 'Scissors'")
'''
A choice will be randomly generated for the computer
```
The result of the game will appear immediately
```
