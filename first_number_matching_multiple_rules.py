# First Number Matching Multiple Rules

found = None

target = int(input("Enter target: "))
n = int(input("How many numbers: "))

for _ in range(n):
    number = int(input("Enter number: "))

    if number > target and number % 2 == 0 and number % 3 == 0:
        found = number
        break

if found is None:
    print("No matching number was found")
else:
    print("First matching number:", found)