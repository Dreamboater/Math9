# Main program to find GCF without functions
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Apply Euclidean algorithm to find GCF
while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

print(f"The Greatest Common Factor is {num1}")
