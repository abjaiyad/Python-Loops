# Find the First Number Greater Than a Target

found = None

target_number = int(input("Enter target: "))
n = int(input("How many numbers: "))

for _ in range(n):

    number = int(input("Enter number: "))

    if number > target_number:
        found = number
        break

if found is None:
    print(f"No number greater than {target_number} was found")
else:
    print(f"First number greater than {target_number}: {found}")