number = int(input("Please type in a number: "))
first_counter = 1
while first_counter <= number:
    second_counter = 1
    # print(f"{first_counter} and {second_counter} and {number}")
    while second_counter <= number:
        print(f"{first_counter} * {second_counter} = {first_counter * second_counter}")
        second_counter += 1
    first_counter += 1



