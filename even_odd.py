# Write a program that displays even numbers 1 to 50 and odd numbers 51 to 100 using a repeating loop.

# Initialize a varible to start at 1
num = 1

# Use while loop to iterate until the number reaches 100
while num <= 100:
    if num <= 50:
        if num % 2 == 0:
            print("Even:", num)
    else:
        if num % 2 != 0:
             print("Odd:", num)
    num += 1