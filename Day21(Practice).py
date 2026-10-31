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

# Check if element exists

t = (10, 20, 30, 40)
if 20 in t:
    print("Found")
else:
    print("Not Found")

#### Convert list into tuple
numbers = [10, 20, 30, 40]
t = tuple(numbers)
print(t)

# Conctenate Two Value
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

#  Find Maximum and mininum

numbers = (45, 12, 78, 23, 90)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Nested tuple
t = ((1,2), (3,4), (5,6))
print(t[0])
print(t[1][1])
print(t[2][0])

#  Remove  an element from tuple
t = (10, 20, 30, 40)
lst = list(t)
lst.remove(20)
t= tuple(lst)
print(t)

#  Important question 
#  1. Find the second largest elements
t = (10, 20, 30, 40,)
unique = set(t)
unique.remove(max(unique))

# 2. Find the Largets and smallest elements
t = (12, 45, 7, 89, 23)
largest = max(t)
smallest = min(t)
print("largest:", largest)
print("smallest:", smallest)
