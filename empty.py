

# #unit converter
# print("welcome to the unit converter app")
# print("Choose the menu:\n 1) Kilometers to Miles \n 2) Celsius to Fahrenheit \n 3) Kilograms to Pounds") 
# try:
#     userInput = int(input("Enter your choice (1/2/3): "))
#     if userInput == 1:
#         Kilometers = float(input("Enter the value of KM"))
#         miles = Kilometers * 0.621371
#         print(f"kilometers: {Kilometers} \n Miles: {miles}")
#     elif userInput == 2:
#         Celsius = float(input("Enter the censius value: "))
#         fahrenheit = (Celsius * 9/5) + 32
#         print(f"Celsius: {Celsius} \n Fahrenheit: {fahrenheit}")
#     elif userInput == 3:
#         kilograms = float(input("Enter the weight in Km: "))
#         pounds=kilograms * 2.20462
#         print(f"Kilograms: {kilograms} \n Pounds: {pounds}")
#     else:
#         print("please enter the number correctly (1/2/3)")
# except ValueError:
#     print("An error has occured")


# #tip calculator
# print("Welcome to the tip calculator ")
# try:
#     billAmt = float(input("Enter the bill amount: "))
#     tipPercent = float(input("Enter the tip percent: "))
    
#     if billAmt < 0 or tipPercent < 0:
#         print("Please enter the positive values only!")
#     else:
#         tipamount = (tipPercent / 100) * billAmt
#         totalAmount = billAmt + tipamount
#         print(f"Tip amount: {tipamount:.2f}")
#         print(f"Total amount to pay: {totalAmount:.2f}")
# except ValueError:
#     print("an error has occured")


# #simple interest calculator
# print("Welcome to the simple interest calculator app")
# try:
#     Principal = float(input("Enter the amount: "))
#     Time = float(input("Enter the time in years: "))
#     Rate = float(input("Enter the rate: "))
        
#     if Principal < 0 or Time < 0 or Rate < 0:
#         print("Please enter the positive value ")
#     else:
#         SimpleInterest = (Principal * Time * Rate)/ 100
#         totalAmt = Principal + SimpleInterest
#         print(f"Simple interest: {SimpleInterest:.2f}")
#         print(f"The total amount after {Time} is {totalAmt:.2f}")
# except ValueError:
#     print("An error has occured!")



# #palindrome checker
# print("Welcome to Palindrome checker!")

# try:
#     Word = input("Enter the word: ").lower().strip()
#     reversedWord = Word[::-1]
#     if Word == reversedWord:
#         print(f"Given word {Word} is a Palindrome")
#     else:
#         print(f"Given word {Word} is not a Palindrome")
# except ValueError:
#     print("An error has been occured, PLease try again!")
    
    
    
# # Currency Converter (Beginner Version)
# print("Welcome to the Currency Converter App!")
# print("Supported conversions:")
# print("1) USD to NPR")
# print("2) NPR to USD")
# print("3) EUR to NPR")
# print("4) NPR to EUR")

# try:
#     choice = int(input("Enter your choice (1/2/3/4): "))
#     amount = float(input("Enter the amount to convert: "))

#     if amount < 0:
#         print("Please enter a positive amount.")
#     else:
#         if choice == 1:
#             result = amount * 133.5
#             print(f"{amount} USD = {result:.2f} NPR")
#         elif choice == 2:
#             result = amount * 0.0075
#             print(f"{amount} NPR = {result:.2f} USD")
#         elif choice == 3:
#             result = amount * 145.2
#             print(f"{amount} EUR = {result:.2f} NPR")
#         elif choice == 4:
#             result = amount * 0.0069
#             print(f"{amount} NPR = {result:.2f} EUR")
#         else:
#             print("Invalid choice. Please enter 1, 2, 3, or 4.")
# except ValueError:
#     print("Invalid input. Please enter a number.")
