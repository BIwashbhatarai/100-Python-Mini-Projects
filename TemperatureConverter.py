print("Welcome to the Temperature converter app")

print("Choose the conversion type: ")
print("1) Celsius to Fahrenheit")
print("2) Fahrenheit to Celsius")

try:
    Choice = int(input("Enter your choice(1/2): "))
    if Choice == 1:
        Celsius = float(input("Enter temperature in celsius: "))
        Fahrenheit = (Celsius * 9/5)+ 32
        print(f"Celsius : {Celsius}°C \n Fahrenheit: {Fahrenheit}°F")
    elif Choice == 2:
        Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        Celsius = (Fahrenheit - 32) * 5/9
        print(f"Fahrenheit : {Fahrenheit}°F \n Celsius: {Celsius}°C")
    else:
        print("Please choose the correct option(1/2)")
except ValueError:
    print("An error has occured, Please try again!")