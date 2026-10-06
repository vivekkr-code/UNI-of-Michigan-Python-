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
print('Done!')

# A simple definite loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

#  A difinite loop with string
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# Finding the largest value
print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')

largest_so_far = -1
print('Before:', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After:', largest_so_far)



