# Welcome message
print("Welcome to the Grade 9 Math Coding Test!")

while True:
    print("\nChoose a topic to test:")
    print("1. Calculating the area and perimeter of a rectangle")
    print("2. Simple number pattern")
    print("3. Solving an equation using a variable")
    print("4. Looping through numbers")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        # Test for calculating area and perimeter of a rectangle
        print("\n** Calculate the area and perimeter of a rectangle **")
        print("Write a Python program that calculates the area and perimeter of a rectangle.")
        print("The formula for the area is area = width * height.")
        print("The formula for the perimeter is perimeter = 2 * (width + height).")
        print("Assume the width = 5 and the height = 10.")
        print("Please write the code to calculate and print both area and perimeter.")

        # Simple solution provided by the program
        width = 5
        height = 10
        area = width * height
        perimeter = 2 * (width + height)
        print("\nExpected Output:")
        print(f"Area = {area}")
        print(f"Perimeter = {perimeter}")

    elif choice == '2':
        # Test for Simple Number Pattern (Arithmetic Progression)
        print("\n** Simple Number Pattern **")
        print("Write a Python program that prints the first 10 numbers in the sequence: 2, 4, 6, 8, ...")
        print("This is an arithmetic sequence where each term increases by 2.")
        print("Your code should print the sequence in the form of: 2 4 6 8 ...")

        # Simple solution provided by the program
        print("\nExpected Output:")
        for i in range(2, 21, 2):
            print(i, end=" ")

    elif choice == '3':
        # Test for solving an equation using a variable
        print("\n** Solving an Equation using a Variable **")
        print("Write a Python program to solve for x in the equation: 3x + 7 = 16.")
        print("The program should output the value of x.")
        print("Hint: Rearrange the equation to solve for x.")

        # Simple solution provided by the program
        x = (16 - 7) / 3
        print("\nExpected Output:")
        print(f"x = {x}")

    elif choice == '4':
        # Test for looping through numbers
        print("\n** Looping Through Numbers **")
        print("Write a Python program that loops through numbers 1 to 10 and prints whether each number is odd or even.")

        # Simple solution provided by the program
        for i in range(1, 11):
            if i % 2 == 0:
                print(f"{i} is even")
            else:
                print(f"{i} is odd")

    elif choice == '5':
        print("Thank you for taking the test! Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
