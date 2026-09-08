# First Odd Number Less Than a Target

found = None

target_number = int(input("Enter target: "))
n = int(input("How many numbers: "))

for _ in range(n):
    number = int(input("Enter number: "))

    if number < target_number and number % 2 != 0:
        found = number
        break

if found is None:
    print(f"No odd number less than {target_number} was found")
else:
    print(f"First odd number less than {target_number}: {found}")