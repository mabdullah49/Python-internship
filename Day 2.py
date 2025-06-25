 # 🐍 ProSensia Internship – Day 2 Task

full_name = input("Enter your full name (First Last): ")

space_index = full_name.find(" ")
first_name = full_name[:space_index]
last_name = full_name[space_index+1:]

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"

print(f"\nResults for {num1} and {num2}:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
