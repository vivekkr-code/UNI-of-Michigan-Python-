# Count Vowels in a String
text = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Total vowels:", count)

# Reverse a String
text = input("Enter a word: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
# Find Total and Average Sales
sales = [1200, 1500, 900, 2000, 1800]

total_sales = sum(sales)
average_sales = total_sales / len(sales)

print("Total sales:", total_sales)
print("Average sales:", average_sales)

# Count Frequency of Each Item
numbers = [1, 2, 2, 3, 1, 2, 4, 3]
frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)

# Calculate Factorial
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)