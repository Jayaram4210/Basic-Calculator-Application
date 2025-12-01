#NUMBER GUESSING GAME
#GUESS THE NUMBER BETWEEN A RANGE - SUCH AS BETWEEN 1 AND 100
import random

number_to_guess = random.randint(1, 100)
while True:
  try:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess == number_to_guess:
       print("Correct! you guessed it!")
    elif guess > number_to_guess:
        print("too high")
    else:
        print("too low")
  except ValueError:
    print("Please enter a valid number!")