# Hangman Game
# Page 4 LC 4
import random

from ClearScreen import clearscreen


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


def hangman(chance):
    clearscreen()
    stage = [
        """
           --------
           |      |
           |      O
           |     /|\
           |      |
           |     / \
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stage[chance]


def display_word(word,guessed_letter):
    clearscreen()
    display = ''
    for letter in word:
        if letter in guessed_letter:
            display += letter + ''
        else:
            display += '_'
    return display

def generated_word(word,guessed_letter):
    word_list = ["Cats", "Dog", "to"]
    return random.choice(word_list)

def start_game(guessed_letter=None):
    word = generated_word()
    guessed_letters = set()
    wrong_guesses = set()
    tries = 6
    tries = 0
    real_word = generated_word()
    while tries < 5:
        print(f"\n\t\thangman(tries)")
        print(f"\t\t Word: {generated_word(word,guessed_letter)}")
        user_word = input(f"Enter your word: ").upper()
        if len(user_word) != 1:
            print(f"Input 1 character Only")
        if not user_word.isalpha():
            print(f"Input a Letter Only")
        if user_word in guessed_letter:
            

        for char in user_word:
            if (letter in user_word for letter in real_word):
                print(f"char is in real word and in user word")
            else:
                print(f"char is not in real word and in user word")
                tries = tries + 1


start_game()
