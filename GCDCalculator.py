print("Welcome to GCD finder!")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    if num1 <= 0 or num2 <= 0:
        print("Please enter the positive integer values!")
    else:
        while num2!= 0:
            num1, num2 = num2 , num1 % num2
        print(f"The GCD is {num1}")
except ValueError:
    print("Invalid input! Please enter a valid positive integer.")
