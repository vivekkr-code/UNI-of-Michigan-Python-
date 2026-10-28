######### A tale of two loops

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

print(list(range(len(friends))))

## Lists can be sliced Using:
t = [9, 41, 12, 3, 74, 15]
t[1:3]
t[:4]
t[3:]
t[:]

# Remember : just like in string, the second numbers is "upto but not including"

########## List Methods
x = list()
type(x)
dir(x)

#  Building a list from scratch
#  We can create an empty list and then add elements using the append method
# The List stays in clear order and new elements are added at the end of the list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# Is something in a list?
#  Python provides two operators that let you check if an item is in a list
# These are logical operators that return true or false
# They do not modify the list
some = [1, 9, 21, 10, 16]
9 in some
15 in some
20 not in some

# Lists are in order
#  A list can hold many items and keeps those items in the order until we do something to change the order
#  A list can be sorted(i.e., change its order)
# The sort method (unlike in strings means "sort yourself" )
friends = ['Joseph', 'glenn', 'sally']
friends.sort()
print(friends)
print(friends[1])

#  Built-in Function and lists
# There are a number of functions built into python that take lists as parameters
#  Remember the loops we built? These are much simpler.
nums=[3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total/count
print('Average:', average)

number = list()
while True:
    inp=input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    number.append(value)
average = sum(number)/len(number)
print('Average:', average)

# This one has to have all number in memory this need millions of numbers

######################################          List And String
# Best Friends : strings and Lists
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

print(stuff)
for w in stuff:
    print(w)

# Split breaks a string into parts and produces a list of strings. We think of these as words. We can access a particular word or loop through all the words.


line = 'A lot                    of spaces'
etc=line.split()
print(etc)
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing=line.split(';')
print(thing)
print(len(thing))
#  When you do not specify a delimiter, multiple spaces are treated like one delimiter
#  You can specify what delimiter character to use in the splitting


# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From') : continue
    word = line.split()
    print(word[2])

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)

#  The Double Split Pattern
# Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again
# from stephen.merquard@uct.ac.za Sat Jan 5 09:14:16 2008
# words = line.split()
# email=words[1]