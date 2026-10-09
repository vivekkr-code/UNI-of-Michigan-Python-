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

# String Library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())


#  Searching A string
fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)