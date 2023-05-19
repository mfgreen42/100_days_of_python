

operations = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide",

}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick and operation from the line above: ")


calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("Qhat's the next number?: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(answer, num3)
