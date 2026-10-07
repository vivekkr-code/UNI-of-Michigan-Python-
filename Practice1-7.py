#  Numeric Expression
xx = 72
yy = 12
cc = xx + yy
print(cc)
cc= xx - yy
print(cc)
cc= xx * yy
print(cc)
cc= xx / yy
print(cc)
cc= xx // yy
print(cc)

#  User input
# num = input('Enter a number: ')
# print('You entered', num)

# x = input('Enter a number: ')
# x = int(x)
# if x > 90:
#     print("Grade A")
# elif x > 80:
#     print("Grade B")
# elif x > 70:
#     print("Grade C")
# elif x > 60:
#     print("Grade D")
# else:
#     print("Grade F")


#  Return Value
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


#  Print 5 to 1
num = 5
while num > 0:
    print(num)
    num = num - 1

#  Infinite Loop
# n = 5
# while n > 0:
#     print('Hello World')
#     print('Rinse')

#  Largest Number
largest = -1
print('Before', largest)
for num in [ 34, 63, 12, 5, 3,6]:
    if num>largest:
        largest = num
        print(largest, num)
print('After', largest)

#  Smallest Number

#  Counting in a Loop
#  Summing in a Loop
#  Filtering in a Loop

