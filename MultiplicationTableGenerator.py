# Multiplication Table Generator
print("Welcome to the Multiplication Table Generator!")

try:
    # Taking input from user
    number = int(input("Enter a number to find the multiplication: "))
    limit = int(input("Enter the value up to which you want the multiplication: "))

    # Checking for invalid zero input
    if number == 0:
        print("Please enter any number except zero!")
    else:
        print(f"\nThe multiplication table of {number} is shown below:")
        # Loop to generate the table
        for i in range(1, limit + 1):
            print(f"{number} * {i} = {number * i}")

except ValueError:
    print("Please enter a valid integer number!")
