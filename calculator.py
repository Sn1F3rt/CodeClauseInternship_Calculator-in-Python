def calculate(operation: str, a: float, b: float):
    match operation:
        case "+":
            return a + b

        case "-":
            return a - b

        case "*":
            return a * b

        case "/":
            return round(a / b, 2)

        case "//":
            return a // b

        case "%":
            return a % b

        case _:
            return None


def main():
    operations = ("+", "-", "*", "/", "//", "%")

    print("Calculator")
    print("==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Remainder")

    operation = int(input("\nEnter the operation [1-6]: "))

    if operation not in range(1, 7):
        return print("Invalid operation!")

    operation = operations[operation - 1]

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    res = calculate(operation=operation, a=num1, b=num2)

    print(
        f"\nResult{' (rounded to two decimal places)' if operation == '/' else ''}: {res}"
    )


if __name__ == "__main__":
    main()
