print("Welcome to the LCM finder")

try:
    # Take input of two numbers from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Check if numbers are positive
    if num1 <= 0 or num2 <= 0:
        print("Please enter valid positive numbers!")
    else:
        # Decide the starting point for checking LCM (greater of two numbers)
        if num1 > num2:
            greater = num1
        else:
            greater = num2
        
        # Loop until we find a number divisible by both inputs
        while True:
            if (greater % num1 == 0) and (greater % num2 == 0):
                lcm = greater
                break
            greater += 1
        
        # Print the calculated LCM
        print(f"The LCM of {num1} and {num2} is {lcm}")
except ValueError:
    print("Please enter a valid integer ")
