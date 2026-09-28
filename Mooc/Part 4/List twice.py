items = []

while True:
    
    try:
        new_item = int(input("New item: "))

        if new_item == 0:
            print("Bye!")
            break

        items.append(new_item)
        print(f"The list now: {items}")
        print(f"The list in order: {sorted(items)}")

    except ValueError:
        print("Invalid Input! Please Try Again...")
