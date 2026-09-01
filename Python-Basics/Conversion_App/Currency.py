# Conversion App
# Page 2 LC2
while True:
    print("\n\t\t\t Currency Converter")
    print("\t\t 1. USD to Pounds")
    print("\t\t 2. USD to Euro")
    print("\t\t 3. USD to AED")
    while True:
        try:
            opt = int(input("\tPlease select an option: "))
            if opt in range(1, 6):
                break
            else:
                print("\n\t\t Invalid Option. Please enter a number between 1 upto 5.")
        except ValueError:
            print("\n\t\t Invalid Option: Please try again...")

    if opt == 1:
        print("\n\t USD to Pounds")
        try:
            usdPd = 0.74
            currency = float(input("\tCurrency: "))
            print(f"\t\t 1 USD is {usdPd} Pounds")
            result = currency * usdPd
            print(f"\t\t {currency} USD is {result} Pounds")
        except ValueError:
            print("\n\t\t Currency Converter Error: Please enter a valid currency Amount.")
    elif opt == 2:
        print("\n\t USD to Euro")
        try:
            usdPd = 0.86
            currency = float(input("\tCurrency: "))
            print(f"\t\t 1 USD is {usdPd} Euro")
            result = currency * usdPd
            print(f"\t\t {currency} USD is {result} Euro")
        except ValueError:
            print("\n\t\t Currency Converter Error: Please enter a valid currency Amount.")
    elif opt == 3:
        print("\n\t USD to AED")
        try:
            usdPd = 3.67
            currency = float(input("\tCurrency: "))
            print(f"\t\t 1 USD is {usdPd} AED")
            result = currency * usdPd
            print(f"\t\t {currency} USD is {result} AED")
        except ValueError:
            print("\n\t\t Currency Converter Error: Please enter a valid currency Amount.")
    elif opt == 4:
        pass
    elif opt == 5:
        print("\n\tExiting Program....\tGood Bye")
        exit()
    again = input("\n\tWould you like to continue (y/n)? ")
    if again.lower() != "y":
        exit()
