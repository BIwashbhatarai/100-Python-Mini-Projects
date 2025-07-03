print("Welcome to the age finder!")
try:
    todayYear = int(input("Enter the today year: "))
    birthYear = int(input("Enter your birth year: "))
    if todayYear < birthYear or todayYear < 0 or birthYear < 0:
        print("Error invalid")
    else:
        birthYear = todayYear - birthYear
        print(f"You are {birthYear} years old.")
except ValueError:
    print("Please enter the valid year!")