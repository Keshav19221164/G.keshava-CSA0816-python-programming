def find_largest_number(num1, num2, num3):
    
    largest_number = max(num1, num2, num3)
    return largest_number

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    largest_number = find_largest_number(num1, num2, num3)
    
    
    print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}")

if _name_ == "_main_":
    main()
