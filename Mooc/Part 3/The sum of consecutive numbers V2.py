limit = int(input("Limit: "))
number = 1
current_value = 0
display = ""
while current_value < limit:
    current_value += number
    display += str(number) + " + "
    number = number + 1

print(f"The consecutive sum: {display[:-3]} = {current_value}")

# limit = int(input("Limit: "))
# number = 1
# current_value = 0
# display = "1"
# while current_value < limit:
#     current_value += number
#     number = number + 1
#     display += " + " + str(number)
#
# print(f"The consecutive sum: {display} = {current_value}"
