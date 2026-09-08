# First Positive Number

found = None

n = int(input("How many numbers: "))

for _ in range(n):

    number = int(input("Enter number: "))

    if number > 0:
        found = number
        break

if found is None:
    print("No positive number was found")
else:
    print("First positive number:", found)