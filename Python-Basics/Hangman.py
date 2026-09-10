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


def display_word(word, guessed_letters):
    clearscreen()
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ''
        else:
            display += '_'
    return display


def generated_word():
    word_list = ["Cats", "Dog", "to"]
    return random.choice(word_list)


def start_game():
    word = generated_word()
    guessed_letters = set()
    wrong_guesses = set()
    tries = 6
    while tries > 0:
        print(f"\n\t\t{hangman(tries)}")
        print(f"\t\t Word: {display_word(word, guessed_letters)}")
        print(f"\t\t Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"\t\t Wrong guesses: {', '.join(wrong_guesses) if wrong_guesses else 'None'}")
        print(f"\t\t Tries: {tries}")
        user_word = input(f"Guess Letter: ")
        if len(user_word) != 1:
            print(f"Input 1 character Only")
            continue
        if not user_word.isalpha():
            print(f"Input a Letter Only")
            continue
        if user_word in guessed_letters or user_word in wrong_guesses:
            print(f"Already Guessed this letter.")
            continue
        if user_word in word:
            print(f"Good job! '{user_word}' is in the word.")
        else:
            wrong_guesses.add(user_word)
            print(f"Sorry, {user_word} is not in the word.")
            tries -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nWord: " + display_word(word, guessed_letters))
            print("\n" + "=" * 40)
            print(f"🎉 CONGRATULATIONS! You won! The word was: {word}")
            print("=" * 40)
            break

    else:
        print("\n {hangman(tries)}")
        print(f"💀 GAME OVER! The word was: {word}")


def main():
    while True:
        start_game()

        again = input("Do you want to play again?: ").lower()
        if again not in ["y", "Y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
