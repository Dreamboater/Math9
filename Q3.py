# 3) Modify the following code so that it outputs the correct values.

x = input("Please enter the first number:")
y = input("Please enter the second number:")

# Prompt the user to choose the type of prism
print("Choose the type of prism:")
print("1. Rectangular-based triangular prism")
print("2. Square-based triangular prism")

choice = input("Enter 1 or 2: ")

# Rectangular-based triangular prism
if choice == '1':
    # Input dimensions for the rectangular-based triangular prism
    length = float(input("Enter the length of the prism: "))
    width = float(input("Enter the width of the base (rectangular side): "))
    height = float(input("Enter the height of the triangular base: "))

    # Surface area of rectangular-based triangular prism
    area_triangle = 0.5 * width * height  # Area of the triangle base
    perimeter_triangle = width + 2 * ((height ** 2 + (width / 2) ** 2) ** 0.5)  # Perimeter of the triangle base
    surface_area = 2 * area_triangle + perimeter_triangle * length

    # Volume of rectangular-based triangular prism
    volume = area_triangle * length

    # Output the results
    print(f"\nRectangular-based triangular prism:")
    print(f"Surface Area: {surface_area:.2f}")
    print(f"Volume: {volume:.2f}")

# Square-based triangular prism
elif choice == '2':
    # Input dimensions for the square-based triangular prism
    side = float(input("Enter the side length of the square base: "))
    height = float(input("Enter the height of the triangular base: "))
    length = float(input("Enter the length of the prism: "))

    # Surface area of square-based triangular prism
    area_triangle = 0.5 * side * height  # Area of the triangle base
    perimeter_triangle = 3 * side  # Perimeter of the triangle base (since it's equilateral)
    surface_area = 2 * area_triangle + perimeter_triangle * length

    # Volume of square-based triangular prism
    volume = area_triangle * length

    # Output the results
    print(f"\nSquare-based triangular prism:")
    print(f"Surface Area: {surface_area:.2f}")
    print(f"Volume: {volume:.2f}")

else:
    print("Invalid choice! Please run the program again and select either 1 or 2.")
