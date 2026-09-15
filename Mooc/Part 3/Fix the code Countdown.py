# Fix the code: Countdown
print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:  # number != 0 makes an Infinite loop if negative number entered.
    print(number)
    number -= 1
print("Now!")
