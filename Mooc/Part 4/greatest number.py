def greatest_number(x:int,y:int,z:int):

    if x <= y and y >= z:
        return y
    elif x >= y                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                and x >= z:
        return x
    else:
        return z

if __name__ == "__main__":
    greatest = greatest_number( 1, 1,-100)
    print(greatest)
