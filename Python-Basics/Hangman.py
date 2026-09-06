# Hangman Game
# Page 4 LC 4

from ClearScreen import clearscreen
from get_integer import get_string


def menu():
    clearscreen()
    print("\t\t\tWelcome to Hangman")
    print(f"\t1. Start Game")
    print(f"\t2. Exit")


def options(choice):
    if choice == 1:
        start_game()
    elif choice == 2:
        exit()


def start_game():
    user_word = ''
    while True:
        word = get_string(str(input("Enter a word: ")))
        while True:
            user_word = input("Enter your word: ")
