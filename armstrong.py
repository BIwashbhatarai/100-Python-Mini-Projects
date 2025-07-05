print("Welcome to the armstrong number finder!")
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digits = int(temp % 10)
    sum += digits ** 3
    temp //= 10

if sum == num:
    print(f"The number {num} is an armstrong number")
else:
    print(f"The number {num} is not an armstrong number")