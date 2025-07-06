# Number Reverser App
print("Welcome to the number reverser app.")

try:
    # Take an integer input from the user
    num = int(input("Enter a number: "))
    
    reversed_num = 0  # Variable to store the reversed number
    temp = abs(num)   # Use absolute value to handle negative numbers
    
    # Loop to reverse the digits
    while temp > 0:
        digit = temp % 10  # Get the last digit
        reversed_num = (reversed_num * 10) + digit  # Add digit to reversed_num
        temp //= 10  # Remove the last digit from temp
    
    # If the original number was negative, add the negative sign back
    if num < 0:
        reversed_num = -reversed_num
    
    # Display the reversed number
    print(f"The reversed number is {reversed_num}")
    
except ValueError:
    # Handle invalid input that cannot be converted to integer
    print("An error has occured, Please try again!")
