limit = int(input("Limit: "))
number = 1
current_value = 0

while current_value < limit:
    current_value += number
    number = number + 1

print(current_value)

# while number <= limit:
#     n = limit - number + 1
#     number = (n / 2) * (number + limit)
#
# print(number)
