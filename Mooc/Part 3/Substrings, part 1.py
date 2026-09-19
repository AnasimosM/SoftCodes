word = input("Please type in a string: ")
count = 1  # If count is 0, it will print an empty string
while count <= len(word):
    print(word[0:count])
    count += 1
