sums = 0

while True:
    number = int(input("Enter a number: "))
    if number == -1:
        break
    sums = sums + number

print(f"Sum is, {sums}")
