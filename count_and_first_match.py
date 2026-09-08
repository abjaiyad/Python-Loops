# Count + First Match

even_count = 0
found = None

n = int(input("How many numbers: "))

for _ in range(n):

    number = int(input("Enter number: "))

    if number % 2 == 0:
        even_count += 1
    if found is None and number > 50:
        found = number

print("Even numbers:", even_count)
if found is None:
    print("No number greater than 50 was found")
else:
    print("First number greater than 50:", found)