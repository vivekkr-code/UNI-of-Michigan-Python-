# Breaking out of a loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')