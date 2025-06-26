
#bmi calculator
print("Welcome to the bmi calculator!")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    if weight <= 0 or height <= 0:
        print("The height and the weight can't be zero")
    else:
        BMI = weight / (height ** 2)
        print(f"Your BMI is {BMI:.2f}")
    
    if BMI < 18.5:
        print("You are underweight")
    elif 18.5 <= BMI < 25:
        print("You have a normal body weight")
    elif 25 <= BMI < 30:
        print("You are overweight")
    else:
        print("you are obese")
except ValueError:
    print("Please enter a valid integer number")