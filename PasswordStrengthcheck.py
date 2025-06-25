
import string

def passwordstrengthChecker(password):
    length = len(password)
    hasUpperCase = any((c.isupper()) for c in password)
    hasLowercase = any((c.islower()) for c in password)
    hasDigits = any((c.isdigit()) for c in password)
    hasSpecialSymbol = any((c in string.punctuation) for c in password)
    score = 0
    
    if hasUpperCase:
        score += 1
    if hasLowercase:
        score += 1
    if hasDigits:
        score +=1
    if hasSpecialSymbol:
        score += 1
    
    if score <= 2:
        print("weak❌")
    elif score == 3:
        print("Medium 🥰")
    else:
        print("Strong🚀")
    
    #feedback
    if length < 8:
        print("Make it atleast 8 characters long")
    if not hasUpperCase:
        print("Use uppercase in the password")
    if not hasLowercase:
        print("Use lowercase in the password")
    if not hasSpecialSymbol:
        print("Use the special symbols in the password")
    if not hasDigits:
        print("Use some digits in the password")
    
    print(f"You have scored {score} in this test")
passInput = input("Enter your password to check its strength: ")
passwordstrengthChecker(passInput)
