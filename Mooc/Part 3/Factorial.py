while True:
    number = int(input("Enter a number: "))
    count = 1
    factorial = number
    if number <= 0:
        print("Thanks and bye!")
        break
    while count < number:
        factorial *= (number - count)
        count += 1
    print(f"The factorial of the number {number} is {factorial}")

