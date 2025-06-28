# Currency Converter (Beginner Version)
print("Welcome to the Currency Converter App!")
print("Supported conversions:")
print("1) USD to NPR")
print("2) NPR to USD")
print("3) EUR to NPR")
print("4) NPR to EUR")

try:
    # Take the user's choice of conversion
    choice = int(input("Enter your choice (1/2/3/4): "))
    
    # Take the amount to convert
    amount = float(input("Enter the amount to convert: "))

    # Check for positive amount
    if amount < 0:
        print("Please enter a positive amount.")
    else:
        # Perform conversion based on choice
        if choice == 1:
            result = amount * 133.5
            print(f"{amount} USD = {result:.2f} NPR")
        elif choice == 2:
            result = amount * 0.0075
            print(f"{amount} NPR = {result:.2f} USD")
        elif choice == 3:
            result = amount * 145.2
            print(f"{amount} EUR = {result:.2f} NPR")
        elif choice == 4:
            result = amount * 0.0069
            print(f"{amount} NPR = {result:.2f} EUR")
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
except ValueError:
    # Handle invalid number inputs
    print("Invalid input. Please enter a number.")
