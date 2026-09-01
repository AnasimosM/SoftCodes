# Simple Calculator
# Page 1 LC1.1

print("\t\t\tCALCULATOR")
print("\t1.Add")
print("\t2.Subtract")
print("\t3.Multiply")
print("\t4.Divide")
print("\t5.Exit")

# add = 0
# subtract = 0
# multiply = 0          THESE ARE UNUSED. NO NEED
# divide = 0
# num1 = 0
# num2 = 0
# opt = 0
while True:
    while True:
        try:
            opt = int(input("Option: "))
            if 0 < opt < 5:
                break
            elif opt == 5:
                print("\t\t\tGood Bye...\n")
                exit()
            else:
                print("Wrong input. Please enter a Number from 1 to 5.\n")
        except ValueError:
            print("Wrong input. Please enter a Number.\n")

    # if 0 < opt < 6:        REDUNDANT CHECK
    while True:
        try:
            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))
            break
        except ValueError:
            print("Wrong input. Please enter a Number.\n")

    if opt == 1:
        print("\t\t\tAdd\n")
        result = num1 + num2
        print(f"The sum of {num1} + {num2}: {result}")
        # add = num1 + num2
        # print(f"{num1} + {num2} = {add}")
    elif opt == 2:
        print("\t\t\tSubtract\n")
        result = num1 - num2
        print(f"The difference of {num1} - {num2}: {result}")
        # subtract = num1 - num2
        # print(f"{num1} - {num2} = {subtract}")
    elif opt == 3:
        print("\t\t\tMultiply\n")
        result = num1 * num2
        print(f"The product of {num1} * {num2}: {result}")
        # multiply = num1 * num2
        # print(f"{num1} * {num2} = {multiply}")
    elif opt == 4:
        print("\t\t\tDivide\n")
        if num2 != 0:
            result = num1 / num2
            print(f"The quotient of {num1} / {num2}: {result}")
            # divide = num1 / num2
            # print(f"{num1} / {num2} = {divide}")
        else:
            print("You can't divide by 0...")

    # elif opt == 5:        REDUNDANT CODE. Already Handled Above
    #     print("\t\t\tGood Bye...")
    #     exit()

    again = input("\n\tYou want to continue? (y/n): \n")
    if again.lower() != "y":  # Starts the Loop if 'y'/'Y' is Pressed
        exit()
# else:             REDUNDANT CODE. The Loop can break without it.
#     print("Wrong input, Please enter the correct Option.")

# Instead of using multiple variables for storing
# the result for add, subtract, multiply, divide.
# We can use one Variable for all the results.
