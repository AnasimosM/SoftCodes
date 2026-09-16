limit = int(input("Limit: "))
number = 1
current_sum = 0

while current_sum < limit:
    current_sum += number
    number = number + 1

print(current_sum)
