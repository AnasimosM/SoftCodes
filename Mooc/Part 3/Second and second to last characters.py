word = str(input("Please type in a string: "))
if word[1] == word[-2]:  # if word[1] == word[-2] and len(word) > 1:
    print(f"The second and the second to last characters are {word[1]}")
else:
    print("The second and the second to last characters are different")
