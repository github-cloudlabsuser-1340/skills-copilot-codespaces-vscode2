def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def percentage(a, b):
    if b == 0:
        return "Error! Division by zero."
    return (a / b) * 100

def calculator():
    """
    A simple calculator function that allows the user to perform basic arithmetic operations.

    The user is prompted to select an operation from the following options:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Percentage

    The function then asks the user to input two numbers and performs the selected operation.
    The result of the operation is displayed to the user.

    If the user enters an invalid choice, an error message is displayed.

    Note:
        - The operations 'add', 'subtract', 'multiply', 'divide', and 'percentage' are expected
          to be implemented as separate functions.
        - Division by zero should be handled appropriately in the 'divide' function.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4/5): ").strip()

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result is: {percentage(num1, num2)}%")
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()