import random
print("Welcome to the number guessing game")
randomNum = random.randint(1,30)
attemps = 5
while attemps > 0:
    try: 
        guess = int(input("Enter your guess: "))
        if guess == randomNum:
            print("Congratulations! you have guessed it correctly")
            break
        elif guess < randomNum:
            print("Too low!, Think higher")
            attemps -= 1
            print(f"You have {attemps} attempts left.")
        else:
            print("Too high! Think lower ")
            attemps -= 1
            print(f"You have {attemps} attempts left.")
    except ValueError:
        print("Please enter a valid number!")

print("The game ends!")
print("You did well!" )
print("You are out of the attempts, The correct number was", randomNum)

