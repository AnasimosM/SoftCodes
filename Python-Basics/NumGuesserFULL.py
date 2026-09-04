# Number Guessing Game (Complete with functions and other python features)
# Page 3 LC3.1
import platform
import random
import subprocess


# import time
#
# result_number = 0
# result_memory = 0


def clear():
    if platform.system() == "Windows":
        # time.sleep(2)
        subprocess.run('cls', shell=True)
    else:
        # time.sleep(2)
        subprocess.run('clear', shell=True)


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\t Invalid Choice. Enter an Integer")


def menu():
    print("\n\t\t\t The Numbers Game")
    print("\t 1. Guessing Game")
    print("\t 2. Memory Game")
    print("\t 3. How to Play")
    print("\t 4. High Score")
    print("\t 5. Exit")

    menu_option(get_integer("\nEnter your Choice: "))


def guess_number():
    # global result_number  # Need to be declared again as 'global' variable in function
    print("\t\t 1. Guessing Game\n")
    random_number = random.randint(1, 6)
    attempts = 0
    while True:
        attempts += 1
        user_guess = get_integer(f"Enter your Choice: ")
        if user_guess < random_number:
            print(f"You Guessed too Low. Try Higher")
        elif user_guess > random_number:
            print(f"You Guessed too Higher. Try Lower")
        else:
            print(f"You Guessed Correctly!")
            print(f"The correct guess is {random_number}")
            # if result_number == 0 or attempts < result_number:
            #     result_number = attempts
            return attempts


def how_to_play():
    print("\t 1. Guessing Game")
    print("\t\t>> This mode is simple you have to guess the correct number")
    print("\t\t   with the least amount of attempts")
    print("\t 2. Memory Game")
    print("\t\t>> This game mode tests your memory by giving you a")
    print("\t\t   larger number with each correct guess.")


def guess_memory():
    # global result_memory  # Need to be declared again as 'global' variable in function
    print("\t\t 2. Memory Game\n")
    number_memory = random.randint(1, 9)
    level = 1
    lives = 3
    while lives != 0:
        print(f" Your number is: {number_memory}")
        # time.sleep(2)
        clear()
        user_guess = get_integer(f"What is the number?: ")
        print(f"\t\t\t Current Level: {level}")
        if user_guess != number_memory:
            print(f" Wrong Answer. Try again...")
            # print(f"\t\t Level is {level}")       DEBUG CHECK CODE
            lives -= 1
        elif user_guess == number_memory:
            print(f"You Guessed Correctly! The correct guess is {number_memory}")
            new_digit = random.randint(0, 9)
            number_memory = number_memory * 10 + new_digit
            level = level + 1
    # if result_memory == 0 or level < result_memory:
    #     result_memory = level
    else:
        print(f" You lost. Your highest Level is {level - 1}")
    return level - 1


def menu_option(choice):
    if choice == 1:
        guess_number()
    elif choice == 2:
        guess_memory()
    elif choice == 3:
        how_to_play()
    elif choice == 4:
        high_score()
    elif choice == 5:
        exit()
    else:
        print("\t Invalid Choice. Enter the correct choice.")


def high_score(result_memory, result_number):
    # result_memory = guess_memory()        #These can run the game again, so make them
    # result_number = guess_number()        # a global variables instead

    print("\t\t\t 4.High Score")
    print(f"\t Your high score for Guessing Game is {result_number}")
    print(f"\t Your high score for Memory Game is Level {result_memory}")

    print("Info: High Score will reset to 0 once the program is closed")


def main():
    while True:
        menu()
        go_back = input("\n\t\t Go back to Menu (y/n): ")
        if go_back.lower() != "y":
            exit()


main()
