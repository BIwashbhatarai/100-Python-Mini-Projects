import random

print("Welcome to the number guessing game")

# Generate a random number between 1 and 30
randomNum = random.randint(1, 30)

# Set the number of attempts the user has
attemps = 5

# Loop until user runs out of attempts
while attemps > 0:
    try:
        # Ask the user to input their guess
        guess = int(input("Enter your guess: "))
        
        # Check if the guess is correct
        if guess == randomNum:
            print("Congratulations! you have guessed it correctly")
            break  # Exit the loop if guessed correctly
        
        # If guess is less than the random number
        elif guess < randomNum:
            print("Too low!, Think higher")
            attemps -= 1  # Decrease attempts by 1
            print(f"You have {attemps} attempts left.")
        
        # If guess is more than the random number
        else:
            print("Too high! Think lower")
            attemps -= 1  # Decrease attempts by 1
            print(f"You have {attemps} attempts left.")
    
    # Handle invalid input that cannot be converted to an integer
    except ValueError:
        print("Please enter a valid number!")

# Game over messages
print("The game ends!")
print("You did well!")
print("You are out of the attempts, The correct number was", randomNum)
