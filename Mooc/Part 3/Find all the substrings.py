word = input("Please type in a word: ")
letter = input("Please type in a character: ")
count = word.find(letter)

while True:
    count = word.find(letter, count)
    if count != -1 and len(word) >= count + 3:
        print(word[count:count + 3])
        count += 1
    else:
        break

# while count + 3 <= len(word):
#     if word[count] == letter:
#         print(word[count:count + 3])
#         count += 1
#     count += 1
