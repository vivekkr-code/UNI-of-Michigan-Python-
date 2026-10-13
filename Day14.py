# Count Vowels in a String
text = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Total vowels:", count)
