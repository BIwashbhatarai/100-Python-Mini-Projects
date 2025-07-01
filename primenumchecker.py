# Prime Number Checker (Beginner Friendly Version)

# Print a welcome message
print("Welcome to the prime number checker!")

try:
    # Ask the user to enter a number and convert it to an integer
    number = int(input("Enter a number: "))
    
    # Check if the number is less than or equal to 1 (not prime)
    if number <= 1:
        print(f"The number {number} is not a prime number")
    else:
        # Assume the number is prime unless we find a factor
        isPrime = True

        # Loop from 2 to number - 1 to check for factors
        for i in range(2, number):
            if number % i == 0:
                # If number is divisible by any i, it's not prime
                isPrime = False
                break  # No need to check further, break the loop

        # Print the result based on the isPrime flag
        if isPrime:
            print(f"The number {number} is a prime number")
        else:
            print(f"The number {number} is not a prime number")

# Handle the error if the user does not enter a valid integer
except ValueError:
    print("Please enter a valid integer number")
