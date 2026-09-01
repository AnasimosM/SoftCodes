# Conversion App
# Page 2 LC2

print("\n\t\t\tConversion App")
print("\t1. Temperature")
print("\t2. Currency")
print("\t3. Weight")
print("\t4. Distance")
print("\t5. Exit Program")

while True:
    try:
        opt = int(input("\n\tEnter your choice: "))
        if opt in range(0, 6):
            break
        else:
            print("\tInvalid choice. Please Enter a number between 1 upto 5.")
    except ValueError:
        print("\tInvalid choice. Please Try Again...")
if opt == 1:
    from Temprature import *
if opt == 2:
    from Currency import *
if opt == 3:
    print("\n\t\t\tWeight Converter not Implemented3")
    # from Weight import *
if opt == 4:
    print("\n\t\t\tDistance Converter not Implemented")
    # from Distance import *
if opt == 5:
    print("\n\t\t\tExiting Program....")
    exit()
