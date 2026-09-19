word = input("Please type in a string: ")
vowel = ["a", "e", "i", "o", "u"]  # Can be written as vowel = "aeiou"
count = 0
while count < len(vowel):
    if vowel[count] in word:
        print(f"{vowel[count]} found")
    else:
        print(f"{vowel[count]} not found")
    count += 1
