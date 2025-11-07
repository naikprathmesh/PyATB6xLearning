# Given a Number a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

number = int(input("Enter Number: "))
factorial = 1
if number > 0:
    for i in range(1,number+1):
        factorial = factorial * i
        print(factorial)
else:
    print("Invalid Number")