year = int(input("Year: "))
year2 = year + 1

while True:
    if year2 % 100 == 0:
        if year2 % 400 == 0:
            break
    elif year2 % 4 == 0:
        break
    year2 = year2 + 1

print(f"The next leap year after {year} is {year2}")

# while True:
#     year = int(input("Year: "))
#     year2 = year
#     while True:
#         year2 += 1
#         if year2 % 4 == 0:
#             if year2 % 100 == 0:
#                 if year2 % 400 == 0:
#                     print(f"The next leap year after {year} is {year2}")
#                     break
#             else:
#                 print(f"The next leap year after {year} is {year2}")
#                 break
#     break
