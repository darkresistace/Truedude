#  Module 4: Functions & Modules in Python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

try:
    number = int(input("Enter a Number: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")




