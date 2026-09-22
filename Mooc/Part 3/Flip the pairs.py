number = int(input("Enter a number: "))
count = 1
while count <= number:
    if count % 2 == 0:
        print(count)
        print(count - 1)
    count += 1


