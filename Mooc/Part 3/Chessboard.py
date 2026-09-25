def chessboard(number):
    p1 = ("10" * number)[:number]
    p2 = ("01" * number)[:number]
    count = 1
    while count  <= number:
        if count % 2 != 0:
            print(p1)
        elif count % 2 == 0:
            print(p2)
        count += 1

if __name__ == "__main__":
    chessboard(4)

# def chessboard(size):
#     i = 0
#     while i < size:
#         if i % 2 == 0:
#             row = "10"*size
#         else:
#             row = "01"*size
#         # Remove extra characters at the end of the row
#         print(row[0:size])
#         i += 1
