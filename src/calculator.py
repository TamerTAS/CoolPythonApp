print("🧮 Smart Calculator")

num1 = float(input("Enter first number: "))
op = input("Choose operation (+, -, *, /, %, ^): ")

num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("❌ Cannot divide by zero")
        exit()
    result = num1 / num2
elif op == "%":
    result = num1 % num2
elif op == "^":
    result = num1 ** num2
else:
    print("❌ Invalid operator")
    exit()

print("✅ Result:", result)
