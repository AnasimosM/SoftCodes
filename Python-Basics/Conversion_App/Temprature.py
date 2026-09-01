# Conversion App
# Page 2 LC2

while True:
    print("\n\t\t\tTemperature")
    print("\nOptions:")
    print("\t\t1.Celsius to Fahrenheit")
    print("\t\t2.Fahrenheit to Celsius")
    print("\t\t3.Celsius to Kelvin")
    print("\t\t4.Kelvin to Celsius")
    print("\t\t5.Fahrenheit to Kelvin")
    print("\t\t6.Kelvin to Fahrenheit")
    print("\t\t7.Back to Menu")
    print("\t\t8.Exit Program")

    while True:
        try:
            opt = int(input("\tPlease select an Option: "))
            if opt in range(1, 9):
                break
            else:
                print("\tWrong Input! Please enter a number from 1 upto 8\n ")
        except ValueError:
            print("\tWrong Input! Please try again...\n ")

    if opt == 1:
        print("\n\t\t1.Celsius to Fahrenheit")
        try:
            temp = float(input("\tPlease enter the temperature in Celsius: "))
            result = (temp * 9 / 5) + 32
            print(f"{temp} Celsius in Fahrenheit: {result}\n")
        except ValueError:
            print("\tWrong Input! Please try again...\n ")
    elif opt == 2:
        print("\n\t\t2.Fahrenheit to Celsius")
        try:
            temp = float(input("\tPlease enter the temperature in Fahrenheit: "))
            result = (temp - 32) * 5 / 9
            print(f"{temp} Fahrenheit in Celsius: {result}\n")
        except ValueError:
            print("\tWrong Input! Please try again...\n ")
    elif opt == 3:
        print("\n\t\t3.Celsius to Kelvin")
        try:
            temp = float(input("\tPlease enter the temperature in Celsius: "))
            result = temp + 273.15
            print(f"{temp} Celsius in Kelvin: {result}\n")
        except ValueError:
            print("\tWrong Input! Please try again...\n ")
    elif opt == 4:
        print("\n\t\t4.Kelvin to Celsius")
        try:
            temp = float(input("\tPlease enter the temperature in Kelvin: "))
            result = temp - 273.15
            print(f"{temp} Kelvin in Celsius: {result}\n")
        except ValueError:
            print("\tWrong Input! Please try again...\n ")
    elif opt == 5:
        print("\n\t\t5.Fahrenheit to Kelvin")
        try:
            temp = float(input("\tPlease enter the temperature in Fahrenheit: "))
            result = (temp - 32) * 5 / 9 + 273.15
            print(f"{temp} Fahrenheit in Kelvin: {result}\n")
        except ValueError:
            print("\tWrong Input! Please try again...\n ")
    elif opt == 6:
        print("\n\t\t6.Kelvin to Fahrenheit")
        try:
            temp = float(input("\tPlease enter the temperature in Kelvin: "))
            result = ((temp - 273.15) * 9 / 5) + 32
            print(f"{temp} Kelvin in Fahrenheit: {result}\n")
        except ValueError:
            print("\tWrong Input! Please try again...\n ")
    elif opt == 7:
        from Menu import *
    elif opt == 8:
        print("\n\tExiting Program....\tGood Bye")
        exit()
    again = input("\n\tWould you like to continue (y/n)? ")
    if again.lower() != "y":
        break
