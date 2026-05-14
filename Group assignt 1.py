# this is the title
print("Welcome to the Temperature Converter!")
# for the is statement to know what is c and f
degree = ["c","C"]
degree2 = ["f","F"]
# to input a letter for the program

again = "Y"

while again in ["y","Y"]:
    x = input("Type 'C' to convert Celsius → Fahrenheit, or 'F' to convert Fahrenheit → Celsius: ")
    # this is a if statement this is for tell the program which one which
    if x in degree:
    # the number that going in the formula
        y = float(input("Enter temperature in Celsius: "))
    # the formula
        cal = (y*9/5)+32
    # the output and the two decimal at the end
        print(f"{y:.2f}","°C is equal to",f"{cal:.2f}","°F")
    # this is for if you put f
    elif x in degree2:
    # the number that going in the formula
        z = float(input("Enter temperature in Fahrenheit: "))
    # the formula
        fah = (z-32)*5/9
    # the output and the two decimal at the end
        print(f"{z:.2f}","°F is equal to",f"{fah:.2f}","°C")
    # This is for if you put anything but c or f
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

    again = input("Do you want to convert another temperature? (Y/N): ")