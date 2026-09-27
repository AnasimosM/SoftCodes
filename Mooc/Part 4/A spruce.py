def spruce(height:int):
    count = 1
    row = 1
    leaf = "*"
    print("a spruce!")
    while count <= height:
        print((leaf*row).center(height*2))
        count += 1
        row += 2
    print(leaf.center(height*2))


if __name__ == "__main__":
    spruce(5)



# def spruce(height):
#     print("a spruce!")
#     i = 1
#     while i <= height:
#         empty = height - i
#         stars = 2 * i - 1
#         print(" " * empty + "*" * stars)
#         i += 1
#     print(" " * (height - 1) + "*")
