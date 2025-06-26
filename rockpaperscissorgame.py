
import random
print("Welcome to the rock paper scissor game: ")
wins = 0
loses = 0 
tie = 0
while True:
    try:
        computerChoice = random.choice(["Rock", "Paper", "Scissor"]).lower()
        userInput = input("Enter (rock/paper/scissor): ").lower()
        if userInput == computerChoice:
            print(f"User chose {userInput} and computer chose {computerChoice}")
            print("Its a Tie")
            tie += 1
        elif userInput == "rock" and computerChoice == "scissor":
            print(f"User chose {userInput} and computer chose {computerChoice} so")
            print("User wins!")
            wins += 1
        elif userInput == "paper" and computerChoice == "rock":
            print(f"User chose {userInput} and computer chose {computerChoice} so")
            print("User wins!")
            wins += 1
        elif userInput == "scissor" and computerChoice == "paper":
            print(f"User chose {userInput} and computer chose {computerChoice} so")
            print("User wins!")
            wins += 1
        elif userInput.lower() == "exit":
            print("Thanks for playing")
            print(f"\n wins : {wins} \n loses : {loses} \n tie : {tie}")
            break
        else:
            print("Computer wins!")
            loses += 1
    except ValueError:
        print("Please choose (rock, paper, scissors)")
