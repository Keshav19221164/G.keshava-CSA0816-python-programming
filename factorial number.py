def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
result = factorial_iterative(number)
print(f"The factorial of {number} is: {result}")
