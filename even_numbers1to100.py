# Write a program that prints all even numbers from 1 to 100.

# Solution: 1
# Initialize a variable to start at 1
# num = 1

# Use a while loop to iterate until the numbers reaches 100
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1

# Solution: 2
# Initialize a variable to start at 2
even = 2
# Use a while loop to iterate until the numbers reaches 100
while even <= 100:
    print(even)
    even += 2

# Solution: 3
# Use a for loop to iterate through the even numbers from 2 to 100
for even in range(2, 101, 2):
    print(even)