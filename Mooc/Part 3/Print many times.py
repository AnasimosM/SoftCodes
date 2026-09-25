def print_many_times(text,number):
    # print((text + "\n") * number)
    while number > 0:
        print(text)
        number -= 1


if __name__ == "__main__":
    print_many_times("python", 5)
