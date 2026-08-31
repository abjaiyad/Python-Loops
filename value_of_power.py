# Write a program that calculates and displays the value of the power of a number entered by the user raised to an 
# exponent also entered by the user, using repetition loops

# Prompt the user for the base number and the exponent
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Initialize the result variable to hold the calculated value
result = 1

# Use a for loop to iterate from 1 to exponent
for _ in range(1, exponent + 1):
    # Multiply the result by the base number in each iteration
    result = result * base

# Display the calculated result
print("The result of", base, "raised to the power of", exponent, "is:", result)