password = input("Password: ")

while True: 
    password = password.replace(" ", "")
    repeat = input("Repeat Password: ")
    if password == repeat:
        break
    print("They do not match!")

print("User account created!")
