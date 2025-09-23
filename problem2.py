# Author: Amad Bin Jaiyad
"""
Problem2:
         Print the multiplication table of a given number using a while loop.
"""
num = int(input("Enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1