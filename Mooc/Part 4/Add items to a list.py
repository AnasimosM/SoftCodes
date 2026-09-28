items = []
amount_items = int(input("How many items: "))
count = 0

while count < amount_items:
    count += 1
    items.append(int(input(f"Item {count}: ")))

print(items)


# numbers = int(input("How many items: "))
# list = []
 
# while len(list) < numbers:
#     number = int(input(f"Item {len(list) + 1}: "))
#     list.append(number)
 
# print(list)
