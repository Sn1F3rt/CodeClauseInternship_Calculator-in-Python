def calculate(operation: str, a: float, b: float):
    # Calculate and return the result based on the operation
    match operation:
        case "+":
            return a + b

        case "-":
            return a - b

        case "*":
            return a * b

        case "/":
            # Round division results to a maximum of two decimal places
            return round(a / b, 2)

        case "//":
            return a // b

        case "%":
            return a % b

        case "**":
            return a ** b

        case _:
            return None


def main():
    # Pre-define possible operations
    operations = ("+", "-", "*", "/", "//", "%", "**")

    print("Calculator")
    print("==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Remainder")
    print("7. Exponent")

    # Prompt the user for their choice of operation
    operation = int(input("\nEnter the operation [1-7]: "))

    # Check if the operation number entered is valid
    if operation not in range(1, 8):
        return print("Invalid operation!")

    operation = operations[operation - 1]

    # Prompt the user for the operands
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Calculate the result
    res = calculate(operation=operation, a=num1, b=num2)

    print(
        f"\nResult{' (rounded to two decimal places)' if operation == '/' else ''}: {res}"
    )


if __name__ == "__main__":
    main()
