items = []

while True:
    print(f"The list is now {items}")
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "d":         
        items.append(len(items) + 1)
    elif items != [] and choice == "r":
        items.pop(-1)
    elif choice == "x":
        print("Bye!")
        break
    else:
        print(f"Invalid Choice! Please Try again...")
