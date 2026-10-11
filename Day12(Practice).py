# Reading and converting 
name = input('Enter: ')
print(name)
apple = input("Enter: ")
x = int(apple) - 10
print(x)

#  String cocatenation
a = 'Hello'
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)

#  Using in as a Logical operator
fruit = 'Banana'
'n' in fruit
'm' in fruit
'nan' in fruit

if 'a' in fruit :
    print ('Found it!')

    #  String Comparision
word = 'banana'
if word == 'banana':
    print('All riight, banana.')
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your Word,' + word + ', comes after banana.')
else:
    print('All right, banana.')


############## Day 11 ###############
#  Search And Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)

nstr = greet.replace('o', 'X')
print(nstr)

#  Stripping Whitespace
greet = '   Hello Bob   '
greet.lstrip()
greet.rstrip()
greet.strip()

#  Prefixes
line = 'Please have a nice day'
line.startswith('Please')
line.startswith('p')

