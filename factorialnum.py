# Factorial Finder
print("Welcome to the factorial finder")

try:
    # Take input from user
    num = int(input("Enter a number: "))
    
    # Factorial of 0 and 1 is 1
    if num == 0 or num == 1:
        print(f"The factorial of {num} is 1")
    else:
        factorial = 1
        # Calculate factorial by multiplying numbers from 1 to num
        for i in range(1, num+1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}")
except ValueError:
    print("Enter a valid integer number")
