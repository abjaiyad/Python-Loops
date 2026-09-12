# Pattern: Hollow Square with User Input

# Make the size dynamic:

# Enter size: 6

# Output:

# ******
# *    *
# *    *
# *    *
# *    *
# ******


row = int(input("Enter rows size: "))
column = int(input("Enter columns size: "))

for r in range(row):
    for c in range(column):
        if (r == 0 or r == row - 1) or (c == 0 or c == column - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()