# Repeated Steps
n=5
while n>0:
    print(n)
    n=n-1
print("Blastoff!")
print(n)

# An infinite Loop
n = 5
while n==5:
    print('Hello World')
    print('Rinse')
print('Done!')
quit()

# Breaking out of a Loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# Finishing an Iteration with continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
