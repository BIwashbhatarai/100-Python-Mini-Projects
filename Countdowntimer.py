

#count down timer
import time 
print("Welcome to the countdown timer!")
try:
    seconds = int(input("Enter the time in seconds: "))
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Times off!")
except ValueError:
    print("Please enter a valid number!")
