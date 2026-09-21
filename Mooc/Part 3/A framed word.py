word = input("Word: ")
frame = "*" * (6 + len(word))
middle = "*" + word.center(len(frame) - 2) + "*"
print(frame) 
print(middle)
print(frame)

print("Length of the String is: " + str(len(word)))

# frame = "*" * 30
# print(frame)
# print("*" + word.center(30 - 2) + "*")
# print(frame)
