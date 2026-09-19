block = "#"
# place = "*"
count = 0
height = int(input("Size of the Pyramid: "))

while height >= count:
    print((block + (block * count)).center(height + 1))
    count += 2

# Only displays pyramid with an odd number base.
