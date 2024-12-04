def calculator():
    print("Calculator")

    # შეიყვანეთ პირველი რიცხვი
    num1 = float(input("Enter the first number: "))

    # შეიყვანეთ მეორე რიცხვი
    num2 = float(input("Enter the second number: "))

    # შეიყვანეთ სიმბოლო გამრავება გაყოფა მიმატება გამოკლება
    operation = input("Enter the operation (+, -, *, /): ")

    # შეასრულეთ გამოთვლა შეყვანილი ოპერაციის მიხედვით
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


calculator()
