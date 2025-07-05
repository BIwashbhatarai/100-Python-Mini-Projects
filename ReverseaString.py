print("Welcome to the reverse string maker")

try:
    word = input("Enter a word: ").strip()
    if not word:
        print("You haven't entered anything")
    else:    
        reversedStr = word[::-1]
        print(f"The word {word} in reversed form is {reversedStr}")
        print("Thanks for using the reverse string app")
        
except ValueError as e:
    print("An error has occured!")