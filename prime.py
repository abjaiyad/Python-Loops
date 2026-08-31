# Write a program that asks the user for a number N and says whether it is prime or not.

# Prompt the user for a number
num = int(input("Enter a number: "))

# Check if the number is less than 2 (not prime)
if num < 2:
    is_prime = False
else:
    is_prime = True

    # Check if the number is divisible by any integer
    # from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % 1 == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print(num, "is a prime")
else:
    print(num, "is not a prime")