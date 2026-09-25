number = int(input("Enter a number: "))
count = 1
while count <= number:
    if count % 2 == 0:
        print(count)
        print(count - 1)
    count += 1
if number % 2 != 0:
    print(count-1)


# index = 1
# while index+1 <= number:
#     print(index+1)
#     print(index)
#     index += 2
 
# if index <= number:
#     print(index)
