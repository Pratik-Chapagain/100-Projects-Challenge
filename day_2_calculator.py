def add (a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide (a,b):
    if b!= 0:
        return a/b
    else:
        return("b mustnot be zero")
    

print("Simple Calculator")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose Operation (+,-,*,/):")


if operation == "+":
    print("Result:", add(num1,num2))
elif operation == "-":
    print("Result:", subtract(num1,num2))
elif operation == "*":
    print("Result:", multiply(num1,num2))
elif operation =="/":
    print("Result:", divide(num1,num2))
else:
    print("Invalid Operation")

