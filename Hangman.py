import random  # Importing the random module to choose a random word

print("Welcome to the Hangman Game!")

# List of words to choose from (all lowercase for consistency)
words = ["apple", "banana", "cherry", "onion"]
secret_word = random.choice(words)  # Randomly selecting one word
guessed_letters = []  # To store letters guessed by the user
attempts = 6  # Total number of wrong attempts allowed

# Main game loop
while attempts > 0:
    display_word = ""  # Word to display with guessed letters and underscores

    # Loop through each letter of the secret word
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "  # Show guessed letter
        else:
            display_word += "_ "  # Show underscore for unguessed letter

    print("Word:", display_word.strip())  # Display the current word

    # Get user's guess
    guess = input("Enter your guess: ").lower().strip()

    # Validate input: only one alphabet character allowed
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    # If letter already guessed
    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(guess)  # Add the guessed letter to the list

    if guess in secret_word:
        print("Good guess!")  # Correct guess
    else:
        attempts -= 1  # Wrong guess, reduce attempts
        print(f"Wrong guess! Attempts left: {attempts}")

    # Check if all letters have been guessed
    if all(letter in guessed_letters for letter in secret_word):
        print(f"🎉 Congratulations! You guessed the word: {secret_word}")
        break

# If the user runs out of attempts
if attempts == 0:
    print(f"😢 You ran out of attempts. The word was: {secret_word}")
