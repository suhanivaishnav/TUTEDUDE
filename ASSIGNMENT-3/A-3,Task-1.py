# Task 1: Calculate Factorial Using a Function

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Calling the function with a sample number
number = 5
result = factorial(number)

print(f"The factorial of {number} is: {result}")
