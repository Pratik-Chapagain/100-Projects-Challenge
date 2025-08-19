def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b


print("=== Simple Calculator ===")
print("Type 'exit' anytime to quit.\n")

while True:
    # ask first number
    num1_input = input("Enter the first number: ")
    if num1_input.lower() == "exit":
        print("Goodbye 👋")
        break
    try:
        num1 = float(num1_input)
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    # ask second number
    num2_input = input("Enter the second number: ")
    if num2_input.lower() == "exit":
        print("Goodbye 👋")
        break
    try:
        num2 = float(num2_input)
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    # ask operation
    operation = input("Choose Operation (+, -, *, /, **, %): ")
    if operation.lower() == "exit":
        print("Goodbye 👋")
        break

    # perform calculation
    if operation == "+":
        print("Result:", add(num1, num2))
    elif operation == "-":
        print("Result:", subtract(num1, num2))
    elif operation == "*":
        print("Result:", multiply(num1, num2))
    elif operation == "/":
        print("Result:", divide(num1, num2))
    elif operation == "**":
        print("Result:", power(num1, num2))
    elif operation == "%":
        print("Result:", modulus(num1, num2))
    else:
        print("❌ Invalid Operation")

    print()  # blank line for readability
