word = input("Please type in a word: ")
character = input("Please type in a character: ")

count = word.find(character)
if count != -1 and len(word) >= count + 3:
    print(word[count:count + 3])

# while True:
#     if word.find(letter) >= len(word) - 2:
#         break
#     elif letter in word:
#         print(word[int(word.find(  letter)):int(word.find(letter)) + 3])
#         break
#     else:
#         break
