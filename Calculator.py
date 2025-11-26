# Simple Python Calculator for QPython
print("Welcome to Asmita's Calculator!")
print("Options: Add, Subtract, Multiply, Divide")


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Choose operation (Add/Subtract/Multiply/Divide): ")


# Convert input numbers to float
try:
    num1 = float(num1)
    num2 = float(num2)
except:
    print("Error! Please enter valid numbers.")
    exit()


# Perform calculation
if operation.lower() == "add":
    result = num1 + num2
elif operation.lower() == "subtract":
    result = num1 - num2
elif operation.lower() == "multiply":
    result = num1 * num2
elif operation.lower() == "divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operation!"


* print("Result:", result)