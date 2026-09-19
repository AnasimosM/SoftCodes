word = input("Please type in a string: ")
count = len(word) - 1
while count >= 0:
    print(word[count:])
    count -= 1
