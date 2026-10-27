#  Programming 
#  Algorithm : A set of rules or steps used to solve a problem
#  Data Structure : A Particular way of organising data in a somputer

#  What is NOT a "Collection"?
x=2
x=4
print(x)

#  A List is a kind of collection
#  A collection allow us to put many values in a single "Variable"
#  A collection is nice because we can carry many values around in one convenient package.
friend=[ 'Joseph', 'Glenn', 'Sally' ]
carryon = [ 'socks', 'shirt', 'perfume' ]

##############################  List Constants
#  List constants are surrounded by square brackets and the elements in the list are separated by commas
#  A list element can be any Python object-even another list
#  A list can be empty

print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([1, [5,6], 7])
print([])

#  We already use lists!
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

# List and definite Loops - Best pals
friends = ['Josheph', 'Glenn', 'Belly']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

x = ['Joseph', 'Glenn', 'Sally']
for x in x:
    print('Happy New year:', x)
print('Done!')

# Looking inside Lists
# Just like strings, we can get at any single element in a list using an index specific in square brackets
friends = ['Joseph', 'Glenn', 'Sally' ]
print(friend[1])

#  List are Mutable
# String are "immutable"- we cannot change the contents of a string - we must make a new string to make any changes
# Lists are "mutable" - we can change an element of a list using the index operator 
fruit = 'banana'
fruit[0] = 'b'
# error
x = fruit.lower()
print(x)
lotto=[2, 14, 26, 41, 63]
print(lotto)
lotto[2]
print(lotto)

#  How long is a list
# The len() function takes a list as a parameter and returns the number of elements in the list
# Actually len() tells us the number of elements of any set or sequence
greet = 'Hello Bob'
print(len(greet))
x = [1, 2, 'joe', 99]
print(len(x))

#  Using the Range Function
# The range function returns a list of numbers that range from zero to one less than the parameter
# We can construct an index loop using for and an integer iterator

print(range(4))
friends = ['Joseph', 'Glenn', 'Sally' ]
print(len(friends))
print(list(range(len(friends))))

