# Write a Python program that automatically generates and displays multiplication tables for numbers 1 through 10.

# Use a nested for loop to iterate through the range 1 to 11
 # For both multiplicands
for i in range(1, 11):
    for j in range(1, 11):
        # Calculate the product of the two numbers
        product = i * j

        # Display the multiplication table entry
        print(i, "*", j, "=", product)

    # Print a separator between each multiplication table
    print("-" * 20)