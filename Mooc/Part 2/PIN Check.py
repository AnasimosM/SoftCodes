PIN = 4321
attempts = 0

while True:  # attempts != 0
    user_input = int(input("PIN: "))
    attempts += 1
    if user_input == PIN:
        if attempts > 1:
            print(f"Correct! It took you {attempts} attempts")
            break
        else:
            print("Correct! It only took you one single attempt!")
            break
    print("Wrong")

# else:
#     print("Too many attempts...")
#     print("Closing Program...")
