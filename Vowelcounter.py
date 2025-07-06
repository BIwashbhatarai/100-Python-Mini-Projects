# Vowel Counter App
print("Welcome to the vowel counter!")

try:
    # Ask the user to enter a word or sentence
    text = input("Enter a word or sentence: ")
    
    # Check if the input is empty
    if not text:
        print("You have entered nothing!")
    else:
        # Define vowels to search for
        vowels = "aeiouAEIOU"  # Included uppercase vowels for completeness
        vowelFound = 0

        # Loop through each letter in the input
        for lett in text:
            if lett in vowels:
                vowelFound += 1
        
        # Show the total number of vowels found
        print(f"The number of vowels found is {vowelFound}")
except Exception as e:
    # Handle any unexpected error
    print("An error has occurred, Please try again")
