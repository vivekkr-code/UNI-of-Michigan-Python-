# Functions
def thing():
    print('Hello')
    print('Fun')
thing()
print('Zip')
thing()

big= max('Hello world')
print(big)
tiny= min('Hello world')
print(tiny)

# def
def print_lyrics():
    print("Ye dil tm bil kahi")
    print('Lagta nhi hum kya kre.')
print_lyrics()

#  Parameters
def greet(lang):
    if lang=='es':
        print('Hola')
    elif lang=='fr':
        print('Bonjour')
    else:
        print('Hello')
greet('es')
greet('fr')
greet('en')

#  Return Values
def greet():
    return 'Hello'
print(greet(),'Vivek')
print(greet(),'Rahul')

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang =='fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'),'Vivek')
print(greet('es'),'Maria')
print(greet('fr'),'Pierre')


x = 'banana'
y = max(x)
z = y * 2