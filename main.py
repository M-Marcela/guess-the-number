#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
print(logo)

HARD_LEVEL = 10
EASY_LEVEL = 5

def set_dificulty():
    level = input("\nGoose a difficult. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return HARD_LEVEL
    elif level == "hard":
        return EASY_LEVEL
    else:
        print("Incorect input.")
        return 0

def check_guess(guess, answer, turns):
    if guess > answer:
        print ("Too high.")
        return turns -1
    elif guess < answer:
        print ("Too low.")
        return turns -1
    else:
        print (f"You got it. The answer was {answer}.")

def game():
    print ("Welcome to the Number Guessing Game!")
    print ("I'm thinking number between 1 and 100")
    answer = random.randint(1, 100)
    print (f"Psst, the number is {answer}")
    turns = set_dificulty()
    
    guess = 0
    
    while guess != answer and turns != 0:
        print (f"\nYou have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_guess(guess, answer, turns)  
        if turns == 0:
            print("\nYou've run out of guesses, you lose.")
            return
        elif guess != answer:
            print ("Guess again.")

game()
