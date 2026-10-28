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

