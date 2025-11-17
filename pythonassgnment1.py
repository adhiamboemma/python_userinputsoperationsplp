first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
math_operation = input("Enter the math operation (+, -, *, /): ")

if math_operation == "+":
    result = float(first_number) + float(second_number)
    print(f"The result of addition is: {result}")
elif math_operation == "-":
    result = float(first_number) - float(second_number)
    print(f"The result of subtraction is: {result}")
elif math_operation == "*":
    result = float(first_number) * float(second_number)
    print(f"The result of multiplication is: {result}")
elif math_operation == "/":
    if float(second_number) != 0:
        result = float(first_number) / float(second_number)
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid math operation.")