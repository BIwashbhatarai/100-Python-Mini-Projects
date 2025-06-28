# Simple Interest Calculator
print("Welcome to the simple interest calculator app")

try:
    # Get principal amount from user
    Principal = float(input("Enter the amount: "))
    # Get time period in years from user
    Time = float(input("Enter the time in years: "))
    # Get rate of interest from user
    Rate = float(input("Enter the rate: "))
    
    # Check if any input is negative
    if Principal < 0 or Time < 0 or Rate < 0:
        print("Please enter positive values only.")
    else:
        # Calculate simple interest
        SimpleInterest = (Principal * Time * Rate) / 100
        # Calculate total amount after interest
        totalAmt = Principal + SimpleInterest
        
        # Print the simple interest rounded to 2 decimals
        print(f"Simple interest: {SimpleInterest:.2f}")
        # Print total amount rounded to 2 decimals
        print(f"The total amount after {Time} years is {totalAmt:.2f}")

except ValueError:
    # Handle invalid inputs that are not numbers
    print("An error has occurred! Please enter valid numbers.")
