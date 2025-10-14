name = input("Hello! What's your name? ")
print(f"Welcome, {name}! Let's do some calculations.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation: +, -, *, /")
operation = input("Enter your choice: ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

print(f"\n{name}, the result of {num1} {operation} {num2} is: {result}")
