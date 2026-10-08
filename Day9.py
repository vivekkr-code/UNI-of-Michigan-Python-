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