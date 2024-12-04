def calculator():
    print("Calculator")

    # Get the first number from the user
    num1 = float(input("Enter the first number: "))

    # Get the second number from the user
    num2 = float(input("Enter the second number: "))

    # Get the operation symbol from the user
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the operation entered
    if operation == "+":
        result = num1 + num2
        print(f"Result: {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Result: {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Result: {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation!")


# Run the calculator function
calculator()
