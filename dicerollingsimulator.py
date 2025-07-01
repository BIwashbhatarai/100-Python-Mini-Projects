import random  # Importing the random module to generate random numbers

print("Welcome to the simple dice rolling simulator")

while True:
    input("Hit enter to roll the dice")  # Waits for user to press enter
    dice = random.randint(1, 6)  # Generates a random number between 1 and 6
    print(f"You rolled a {dice}")  # Displays the number rolled

    # Asks the user if they want to roll again
    playAgain = input("Do you wanna roll the dice more (yes/no): ").lower()
    if playAgain != "yes":
        print("Thanks for playing, hope you have enjoyed!")
        break  # Exits the loop if user types anything other than 'yes'
