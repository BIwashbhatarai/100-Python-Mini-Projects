# Unit Converter App
print("Welcome to the unit converter app")

# Show menu options to the user
print("Choose the menu:\n 1) Kilometers to Miles \n 2) Celsius to Fahrenheit \n 3) Kilograms to Pounds")

try:
    # Take user input for choice of conversion
    userInput = int(input("Enter your choice (1/2/3): "))
    
    if userInput == 1:
        # Convert Kilometers to Miles
        Kilometers = float(input("Enter the value of KM: "))
        miles = Kilometers * 0.621371
        print(f"Kilometers: {Kilometers} \nMiles: {miles}")
        
    elif userInput == 2:
        # Convert Celsius to Fahrenheit
        Celsius = float(input("Enter the Celsius value: "))
        fahrenheit = (Celsius * 9/5) + 32
        print(f"Celsius: {Celsius} \nFahrenheit: {fahrenheit}")
        
    elif userInput == 3:
        # Convert Kilograms to Pounds
        kilograms = float(input("Enter the weight in Kg: "))
        pounds = kilograms * 2.20462
        print(f"Kilograms: {kilograms} \nPounds: {pounds}")
        
    else:
        # Handle invalid menu option
        print("Please enter the number correctly (1/2/3)")
        
except ValueError:
    # Handle invalid input type error
    print("An error has occurred. Please enter a valid number.")
