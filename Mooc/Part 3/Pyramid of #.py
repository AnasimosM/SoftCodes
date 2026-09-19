# place = "*"

block = "#"
height = int(input("Size of the Pyramid: "))

while height > 0:
    print(" " * height + block)
    block += "##"
    height -= 1

# count = 0
# while height >= count:
#     print((block + (block * count)).center(height + 1))
#     count += 2
#
# # Only displays pyramid with an odd number base.
