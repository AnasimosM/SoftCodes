# Number Guessing Game (IF and While)
# Page 3 LC3

import random

print("\t\t\t Number Guessing Game")
print("\t 1. Start Game ")
print("\t 2. Exit Game ")

while True:
    try:
        opt = int(input("Enter your choice: "))
        if opt == 1:
            break
        elif opt == 2:
            exit()
        else:
            print("Please enter a valid number from 1 and 2")  # Output starts Loop again
    except ValueError:
        print("Please enter a Valid Number between 1 and 2")
while True:
    attempt = 0
    gen = random.randint(1, 1000)  # Must be place here outside the Guess Loop
    while True:
        attempt += 1
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please valid number")
            continue
        if guess < gen:
            print("Your guess is too low")
        elif guess > gen:
            print("Your guess is too high")
        else:
            # elif gen == guess:  #Can be else, since it's the last option
            print(f"You guessed right! The number is {guess}")
            print(f"Attempted {attempt} times")
            break

    again = str(input("Do you want to play again? (y/n): "))
    if again.lower() != "y":
        print("Thanks for playing!")
        exit()
