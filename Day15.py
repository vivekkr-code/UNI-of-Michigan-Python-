# Check for a palindrome
text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# Find the second-largest number
numbers = [10, 25, 8, 40, 25, 30]

largest = float('-inf')
second = float('-inf')

for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif largest > n > second:
        second = n

print("Second largest:", second)