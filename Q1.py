# 1.) Modify the following code so it outputs the correct values

# Main program loop
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user input for operation
choice = input("Enter choice (1/2/3/4): ")

# Take user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 - num2
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = num1 + num2
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = num1 / num2
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 * num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input")

# 2. Modify the following code so that it outputs the correct values.
