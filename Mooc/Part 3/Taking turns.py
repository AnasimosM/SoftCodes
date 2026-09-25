number = int(input("Please type in a number: "))
first = 1
Last = number

while first <= Last:

    print(f"{first}")
    first += 1
    if first < Last:
        print(f"{Last}")
        Last -= 1
