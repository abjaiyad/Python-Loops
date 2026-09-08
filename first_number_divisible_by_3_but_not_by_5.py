# First Number Divisible by 3 but NOT by 5

found = None

n = int(input("How many numbers: "))

for _ in range(n):

    number = int(input("Enter number: "))

    if number % 3 == 0 and number % 5 != 0:
        found = number
        break

if found is None:
    print("No number divisible by 3 but not by 5 was found")
else:
    print("First number divisible by 3 but not by 5:", found)