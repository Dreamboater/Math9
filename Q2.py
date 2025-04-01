# Sample linear equation: y = 2x + 3

# Define the range of x values (e.g., from -5 to 5)
x_1 = int(input("Please enter a starting x-value:"))
x_2 = int(input("Please enter an ending x-value:"))


# Loop through each x value and calculate the corresponding y value
for x in range(x_1,x_2):
    y = 2 * x + 3
    print(f"For x = {x}, y = {y}")

# Using the code above as a template solve the following word problem:
# A small business owner sells handcrafted candles. The business has fixed costs of $50 for materials and packaging.
# Additionally, it costs $5 to make each candle.
# The business owner wants to determine the total cost for making and selling a range of different candles.
#
# Write a linear equation for the total cost, and use Python to calculate the total cost for making and selling a
# range of candles as chosen by the user.
