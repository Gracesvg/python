# Create a calculator using elif statement and also using input-output
num1 = float(input("Enter First Number:"))
num2 = float(input("Enter Second Number:"))

operation2 = "+-/*"

operation = operation2 = input("Enter operator:")
if operation2 == "+":
    print(num1 + num2)

elif operation2 == "-":
    print(num1 - num2)
elif operation2 == "*":
    print(num1 * num2)
elif operation2 == "/":
    print(num1 / num2)
