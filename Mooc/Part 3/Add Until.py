sums = 0
while True:
    number = int(input("Enter a number: "))
    sums = sums + number
    if number == -1:
        break
print(f"Sum is, {sums}")
