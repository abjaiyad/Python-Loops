# Author: Amad Bin Jaiyad
"""
Problem5:
         Take a list of numbers and print only the odd ones using a loop.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0:
        print(num)