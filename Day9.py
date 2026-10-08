#  A character too far
zot = 'abc'
print(zot[2])

# Strings have length
fruit = 'banana'
print(len(fruit))

# Length function
fruit = 'apple'
x = len(fruit)
print(x)

# Looking through strings
fruit = 'Apple'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = ' banana'
for letter in fruit:
    print(letter)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# Slicing Strings
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

# USing 'in' as a logical operator
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print('Found it !')