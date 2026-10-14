# Check for a palindrome
text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")