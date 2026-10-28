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
