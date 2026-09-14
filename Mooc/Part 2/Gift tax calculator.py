value = float(input("Value of gift: "))

if value >= 5000:
    if value >= 1000000:
        rate = 0.17
        min_value = 1000000
        limit = 142100
    elif value >= 200000:
        rate = 0.15
        min_value = 200000
        limit = 22100
    elif value >= 55000:
        rate = 0.12
        min_value = 55000
        limit = 4700
    elif value >= 25000:
        rate = 0.1
        min_value = 25000
        limit = 1700
    else:
        rate = 0.08
        min_value = 5000
        limit = 100

    tax = limit + ((value - min_value) * rate)
    print(f"Amount of tax: {tax} euros")

else:
    print("No tax!")
