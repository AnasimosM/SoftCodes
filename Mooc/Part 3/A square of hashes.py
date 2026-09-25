def hash_square(number):
    count = number
    while count > 0:
        print("#" * number)
        count -=1 


if __name__ == "__main__":
    hash_square(5)
