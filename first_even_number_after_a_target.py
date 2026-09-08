# First Even Number After a Target

found = None

target_number = int(input("Enter target: "))
n = int(input("How many numbers: "))

for _ in range(n):
    number = int(input("Enter number: "))

    if number > target_number and number % 2 == 0:
        found = number
        break

if found is None:
    print(f"No even number greater than {target_number} was found")
else:
    print(f"First even number greater than {target_number}: {found}")