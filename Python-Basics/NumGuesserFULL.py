# Number Guessing Game (Complete with functions and other python features)
# Page 3 LC3.1
import platform
import random
import subprocess
import time

result_number = 0
result_memory = 0


def main():
    while True:
        menu()
        go_back = input("\n\t\t Go back to Menu (y/n): ")
        if go_back.lower() != "y":
            exit()
        clear(0)


def clear(value):
    time.sleep(value)
    if platform.system() == "Windows":
        subprocess.run('cls', shell=True)
    else:
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


def menu_option(choice):
    clear(0)
    if choice == 1:
        guess_number()
    elif choice == 2:
        guess_memory(5)
    elif choice == 3:
        how_to_play()
    elif choice == 4:
        high_score(result_memory, result_number)
    elif choice == 5:
        exit()
    else:
        print("\t Invalid Choice. Enter the correct choice.")


class DifficultyManager:
    def __init__(self):
        self.last_difficulty_level = 0

    def difficulty_time(self, difficulty, get_seconds):
        if difficulty % 5 == 0 and difficulty != self.last_difficulty_level:
            self.last_difficulty_level = difficulty
            if get_seconds > 1:
                get_seconds -= 1
                if get_seconds <= 1:
                    get_seconds = 1
                print(f"\t\t\t Difficulty increased!")
                print(f"Time limit to memorize changed to {get_seconds} Seconds...")

        return get_seconds


def guess_number(rank_max=5):
    global result_number  # Need to be declared again as 'global' variable in function
    user_guess = None
    print("\t\t 1. Guessing Game\n")
    guess_level = 1
    attempts = 0
    while True:
        while True:
            random_number = random.randint(1, rank_max)
            print(f"\t\t Current Level: {guess_level} ")  # and number is {random_number}
            print(f" Hidden number is between 1 and {rank_max}")
            attempts += 1
            user_guess = get_integer(f"Enter your Guess: ")
            if user_guess < random_number:
                print(f"You Guessed too Low. Try Higher")
                clear(2)
            elif user_guess > random_number:
                print(f"You Guessed too High. Try Lower")
                clear(2)
            else:
                print(f"You Guessed Correctly!")
                print(f"The correct guess is {random_number}")
                print(f"You took {attempts} attempts to guess the correct number.")
                rank_max = rank_max * 2
                if result_number == 0 or guess_level > result_number:
                    result_number = guess_level
                print(f"Your highest Level is {guess_level - 1}")
                guess_level += 1
                attempts = 0


def guess_memory(seconds):
    global result_memory  # Need to be declared again as 'global' variable in function
    lives = 3
    print("\t\t 2. Memory Game\n")
    number_memory = random.randint(1, 9)
    level = 1
    difficulty_manager = DifficultyManager()
    while lives > 0:
        print(f"\t\t\t Current Level: {level}")
        print(f" Your number is: {number_memory}")
        seconds = difficulty_manager.difficulty_time(level, seconds)
        clear(seconds)
        print(f"\t\t\t❤️ {lives} Lives")

        # print(f"{seconds} Seconds")  # DEBUG CHECK CODE
        user_guess = get_integer(f"Enter your Guess: ")

        if user_guess != number_memory:
            print(f" Wrong Answer. Try again...")
            # print(f"\t\t Level is {level}")       DEBUG CHECK CODE
            lives -= 1
        elif user_guess == number_memory:
            print(f"You Guessed Correctly! The correct guess is {number_memory}")
            new_digit = random.randint(0, 9)
            number_memory = number_memory * 10 + new_digit
            level = level + 1
    print(f" You lost. Your highest Level is {level - 1}")
    if result_memory == 0 or level - 1 > result_memory:
        result_memory = level - 1
    return level - 1


def how_to_play():
    print("\t 1. Guessing Game")
    print("\t\t>> This mode is simple you have to guess the correct number")
    print("\t\t   with the least amount of attempts")
    print("\t 2. Memory Game")
    print("\t\t>> This game mode tests your memory by giving you a")
    print("\t\t   larger number with each correct guess. ")


def high_score(high_memory, high_number):
    # result_memory = guess_memory()        #These can run the game again, so make them
    # result_number = guess_number()        # a global variables instead

    print("\t\t\t 4.High Score")
    print(f"\t Your high score for Guessing Game is Level {high_number}")
    print(f"\t Your high score for Memory Game is Level {high_memory}")

    print("NOTICE: High Score will reset to 0 once the program is closed")


main()
