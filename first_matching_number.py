# First Matching Number

found = None

n = int(input("How many numbers: "))

for _ in range(n):

    num = int(input("Enter number: "))

    if num % 7 == 0:
        found = num
        break

if found is None:
    print("No number divisible by 7 was found")
else:
    print("First number divisible by 7:", found)