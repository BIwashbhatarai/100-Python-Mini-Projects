# BMI Calculator
print("Welcome to the BMI calculator!")

try:
    # Get user's weight in kilograms
    weight = float(input("Enter your weight in kg: "))
    
    # Get user's height in meters
    height = float(input("Enter your height in meters: "))
    
    # Check if weight or height is zero or negative
    if weight <= 0 or height <= 0:
        print("The height and the weight can't be zero or negative")
    else:
        # Calculate BMI = weight divided by height squared
        BMI = weight / (height ** 2)
        print(f"Your BMI is {BMI:.2f}")
        
        # Give feedback based on BMI value
        if BMI < 18.5:
            print("You are underweight")
        elif 18.5 <= BMI < 25:
            print("You have a normal body weight")
        elif 25 <= BMI < 30:
            print("You are overweight")
        else:
            print("You are obese")
except ValueError:
    # Handle if user enters something other than a number
    print("Please enter a valid number!")
