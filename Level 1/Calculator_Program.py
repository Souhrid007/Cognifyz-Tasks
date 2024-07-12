def calculator():
    x = float(input("Enter the first number: "))
    op = input("Enter the operator (+, -, *, /, %): ")
    y = float(input("Enter the second number: "))
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        if y == 0:
            result = "Error: Division by zero!"
        else:
            result = x / y
    elif op == '%':
        result = x % y
    else:
        result = "Error: Invalid operator!"
    print("Result:", result)

calculator()
