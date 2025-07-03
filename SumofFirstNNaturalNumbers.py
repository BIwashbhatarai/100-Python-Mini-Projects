print("Welcome to the sum of the N natural number finder!")
try:
    N = int(input("Enter a number: "))
    if N < 0:
        print("Please add non negative integer!")
    else:
        calculated_sum = int((N * (N + 1)) /2)
        print(f"The sum of the first {N} natural numbers is: {calculated_sum}")
except ValueError:
    print("An error has occured!")