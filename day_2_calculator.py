import math

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

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Cannot calculate square root of a negative number"

def factorial(a):
    if a >= 0 and a.is_integer():
        return math.factorial(int(a))
    else:
        return "Factorial is only defined for non-negative integers"

print("=== Simple Calculator ===")
print("Type 'exit' to quit, 'history' to view past results, or 'cont' to use previous result.\n")

history = []  # Store calculation history
prev_result = None  # Store previous result for continuous mode

while True:
    # Ask for operation
    operation = input("Choose Operation (+, -, *, /, **, %, ^, !, history, cont): ")
    if operation.lower() == "exit":
        print("Goodbye 👋")
        break
    elif operation.lower() == "history":
        if history:
            print("\nCalculation History:")
            for i, calc in enumerate(history, 1):
                print(f"{i}. {calc}")
        else:
            print("No calculations in history.")
        print()
        continue
    elif operation.lower() == "cont" and prev_result is not None:
        num1 = prev_result
        print(f"Using previous result: {num1}")
    else:
        # Ask for first number if not in continuous mode or no previous result
        if operation.lower() != "cont":
            num1_input = input("Enter the number: ")
            if num1_input.lower() == "exit":
                print("Goodbye 👋")
                break
            try:
                num1 = float(num1_input)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
                continue
        else:
            print("❌ No previous result available. Please choose another operation.")
            continue

    # Check if operation requires a second number
    if operation not in ["^", "!", "history", "cont"]:
        num2_input = input("Enter the second number: ")
        if num2_input.lower() == "exit":
            print("Goodbye 👋")
            break
        try:
            num2 = float(num2_input)
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

    # Perform calculation
    result = None
    calc_str = ""
    if operation == "+":
        result = add(num1, num2)
        calc_str = f"{num1} + {num2} = {result}"
    elif operation == "-":
        result = subtract(num1, num2)
        calc_str = f"{num1} - {num2} = {result}"
    elif operation == "*":
        result = multiply(num1, num2)
        calc_str = f"{num1} * {num2} = {result}"
    elif operation == "/":
        result = divide(num1, num2)
        calc_str = f"{num1} / {num2} = {result}"
    elif operation == "**":
        result = power(num1, num2)
        calc_str = f"{num1} ** {num2} = {result}"
    elif operation == "%":
        result = modulus(num1, num2)
        calc_str = f"{num1} % {num2} = {result}"
    elif operation == "^":
        result = square_root(num1)
        calc_str = f"√{num1} = {result}"
    elif operation == "!":
        result = factorial(num1)
        calc_str = f"{int(num1)}! = {result}"
    elif operation.lower() == "cont":
        # Continue mode: ask for new operation
        operation = input("Choose Operation for continuous mode (+, -, *, /, **, %, ^, !): ")
        if operation.lower() == "exit":
            print("Goodbye 👋")
            break
        if operation not in ["^", "!"]:
            num2_input = input("Enter the second number: ")
            if num2_input.lower() == "exit":
                print("Goodbye 👋")
                break
            try:
                num2 = float(num2_input)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
                continue
        if operation == "+":
            result = add(num1, num2)
            calc_str = f"{num1} + {num2} = {result}"
        elif operation == "-":
            result = subtract(num1, num2)
            calc_str = f"{num1} - {num2} = {result}"
        elif operation == "*":
            result = multiply(num1, num2)
            calc_str = f"{num1} * {num2} = {result}"
        elif operation == "/":
            result = divide(num1, num2)
            calc_str = f"{num1} / {num2} = {result}"
        elif operation == "**":
            result = power(num1, num2)
            calc_str = f"{num1} ** {num2} = {result}"
        elif operation == "%":
            result = modulus(num1, num2)
            calc_str = f"{num1} % {num2} = {result}"
        elif operation == "^":
            result = square_root(num1)
            calc_str = f"√{num1} = {result}"
        elif operation == "!":
            result = factorial(num1)
            calc_str = f"{int(num1)}! = {result}"
        else:
            print("❌ Invalid Operation")
            continue
    else:
        print("❌ Invalid Operation")
        continue

    # Store result and update history
    if result is not None:
        print("Result:", result)
        history.append(calc_str)
        prev_result = result if isinstance(result, (int, float)) else None

    print()  # Blank line for readability