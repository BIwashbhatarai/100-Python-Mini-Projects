# Palindrome Checker
print("Welcome to Palindrome checker!")

try:
    # Take input from user, convert to lowercase and remove extra spaces
    Word = input("Enter the word: ").lower().strip()
    
    # Reverse the word using slicing
    reversedWord = Word[::-1]
    
    # Check if the original word and reversed word are the same
    if Word == reversedWord:
        print(f"Given word '{Word}' is a Palindrome")
    else:
        print(f"Given word '{Word}' is not a Palindrome")
except ValueError:
    # Handle unexpected errors in input
    print("An error has occurred, please try again!")
