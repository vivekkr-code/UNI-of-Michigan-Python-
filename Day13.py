# Daily Python Practice
# Topic: Functions

def calculate_square(number):
    return number * number

num = int(input("Enter a number: "))
result = calculate_square(num)

print("Square:", result)

#  Simple calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b if b != 0 else "Cannot divide by zero")

#  Even And Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#  Student marks analysis
marks = [78, 85, 92, 67, 88]

print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
