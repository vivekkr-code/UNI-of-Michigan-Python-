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

