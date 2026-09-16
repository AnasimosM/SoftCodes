limit = int(input("Limit: "))
number = 1
while number <= limit:
    n = limit - number + 1
    number = (n / 2) * (number + limit)

print(number)
