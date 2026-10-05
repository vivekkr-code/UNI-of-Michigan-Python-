# Breaking out of a loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# Finishing an iteration with continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)