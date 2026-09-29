def list_of_stars(amount:int):
    star = "*"
    for i in amount:
        print(star * i)

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])

# def list_of_stars(my_list: list):
#     for number in my_list:
#         print("*" * number)
