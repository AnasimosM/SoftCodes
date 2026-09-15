words = ""
last_word = ""
while True:
    user_input = input("Please type in a word: ")
    user_input = user_input.replace(" ", "")
    if user_input == "end" or user_input == last_word:
        break
    words += user_input + " "
    last_word = user_input

print(words)
