word = input("Please type in a string: ")
substring = input("Please type in a substring: ")

first_index = word.find(substring)
if first_index != -1:
    second_index = word.find(substring, first_index + len(substring))
    if second_index != -1:
        print(f"The second occurrence of the substring is at index {second_index}")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")
