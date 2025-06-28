# Tip Calculator
print("Welcome to the tip calculator")

try:
    # Take bill amount input from the user
    billAmt = float(input("Enter the bill amount: "))
    # Take tip percentage input from the user
    tipPercent = float(input("Enter the tip percent: "))
    
    # Check if inputs are positive values
    if billAmt < 0 or tipPercent < 0:
        print("Please enter positive values only!")
    else:
        # Calculate the tip amount
        tipamount = (tipPercent / 100) * billAmt
        # Calculate the total amount including tip
        totalAmount = billAmt + tipamount
        
        # Print tip amount rounded to 2 decimals
        print(f"Tip amount: {tipamount:.2f}")
        # Print total amount to pay rounded to 2 decimals
        print(f"Total amount to pay: {totalAmount:.2f}")
except ValueError:
    # Handle case when user enters invalid input
    print("An error has occurred. Please enter valid numbers.")