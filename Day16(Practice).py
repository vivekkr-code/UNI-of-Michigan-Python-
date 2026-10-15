# Find the factorial of a number
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)

# Print the Fibonacci series
a, b = 0, 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b