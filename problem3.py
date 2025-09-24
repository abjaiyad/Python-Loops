# Author: Amad Bin Jaiyad
"""
Problem3:
         Keep asking the user to enter a number until they type 0.
"""
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print(f"You entered: {num}")
print("Program ended.")
