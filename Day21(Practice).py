#####################    Tuples

# Basic tuple creation 
t = (10, 20, 30, 40, 50)
print(t)
print(type(t))
print(len(t))

# Access tuple elements
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[2])
print(numbers[-1])

#  Tuples Slicing 
t = (10, 20, 30, 40, 50, 60)
print(t[1:4])
print(t[:2])
print(t[3:])
print(t[::-1])

# Count and index
t = (10, 20, 30, 20, 40, 20)
print(t.count(20))
print(t.index(30))

# Tuple iteration
fruits = ("apples", "banana", "mango","orange")
for fruit in fruits:
    print(fruit)

