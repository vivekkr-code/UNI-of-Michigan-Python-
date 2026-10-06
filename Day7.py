#  Finding the largest number
largest_so_far = -1
print('Before:', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After:', largest_so_far)

smallest = 100
for num in [56, 35, 9, 95, 69, 8]:
    if num < smallest:
        smallest = num
    print(smallest, num)
print("After", smallest)

# Counting in a loop
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

count = 0
for num in [8, 84, 41, 67, 73, 883, 3]:
    count = count + 1
    print(count,num)
    print("After", count)

# Summing in a loop
total = 0
print('Before', total)
for thing in [9, 41, 12, 3, 74, 15]:
    total = total + thing
    print(total, thing)
print('After', total)

# filtering in a loop
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')