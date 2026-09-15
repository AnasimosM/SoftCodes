number = 5
print("Countdown!")

while True:
    if number != 0:
        print(number)
        number -= 1
        if number == 0:
            print("Now!")
    else:
        break
