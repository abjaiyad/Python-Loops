# Palindrome checker

number = int(input("Enter number: "))

original = number
palindrome = 0

while number:
    digit = number % 10
    number //= 10
    palindrome = palindrome * 10 + digit

if original == palindrome:
    print("Palindrome:", palindrome)
else:
    print("Not palindrome:", palindrome)