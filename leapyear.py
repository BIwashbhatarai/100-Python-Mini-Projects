print("Welcome to the leap year calculator")
try:
    year = int(input("Enter the year: "))
    
    if year < 0:
        print("Year cannot be negative")
    else:
        if year % 400 == 0:
            print(f"The year {year} is a leap year")
        elif year % 100 == 0:
            print(f"The year {year} is not a leap year")
        elif year % 4 == 0:
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")
except ValueError:
    print("Please enter a valid integer value")