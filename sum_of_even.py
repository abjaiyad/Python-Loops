# Write a program that calculates and displays the sum of even numbers from 1 to 100 using a repeating loop.

# Initialize variables
sum_of_evens = 0
num = 2

# Use a while loop to iterate until num reaches 100
while num <= 100:
    # Add the current number to the sum if it is even
    sum_of_evens += num

    # Increment the number by 2 to get next even number
    num += 2

# Display the sum of even numbers
print("The sum of even numbers from 1 to 100 is:", sum_of_evens)