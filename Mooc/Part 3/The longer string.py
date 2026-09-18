word1 = str(input("Please type in string 1: "))
word2 = str(input("Please type in string 2: "))

if len(word1) > len(word2):
    print(f"{word1} is longer")
elif len(word1) < len(word2):
    print(f"{word2} is longer")
else:
    print("The strings are equally long")
