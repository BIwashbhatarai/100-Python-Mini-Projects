print("Welcome to the power calculator!")
try:
    base = float(input("Enter the base value: "))
    exponent = int(input("Enter the power value: "))
    
    if exponent == 0:
        print(f"{base} raised to the power of {exponent} is 1")
    else:
        result = base ** exponent
        print(f"{base} raised to the power of {exponent} is {result}")
        
except ValueError:
    print("An error has occured")
    