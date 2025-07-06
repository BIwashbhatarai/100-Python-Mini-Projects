# Print a welcome message
print("Welcome to the odd or even checker!")

try:
    # Take input from the user and convert it to an integer
    num = int(input("Enter a number: "))
    
    # Check if the number is divisible by 2 (even)
    if num % 2 == 0:
        print(f"The given number {num} is an even number!")
    else:
        # If not divisible by 2, then it's odd
        print(f"The given number {num} is an odd number!")

# Handle the case where the user doesn't enter a valid integer
except ValueError:
    print("An error has occured, Please try again later")
