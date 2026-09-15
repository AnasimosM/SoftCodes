count = 0
sums = 0
positive = 0
print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))

    if number > 0:
        positive += 1

    if number == 0:
        break

    count += 1
    sums += number

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sums}")
print(f"The mean of the numbers is {sums / count}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {count - positive}")
