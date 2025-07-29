# Simple calculator by Purity

print("Welcome to my calculator!")

a = input("Type first number: ")
b = input("Type second number: ")
op = input("Choose operation (+, -, *, /): ")

x = float(a)
y = float(b)

if op == "+":
    ans = x + y
elif op == "-":
    ans = x - y
elif op == "*":
    ans = x * y
elif op == "/":
    if y != 0:
        ans = x / y
    else:
        ans = "Error: Division by zero!"
else:
    ans = "Invalid operator!"

print("Answer:", ans)
