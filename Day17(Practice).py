# Find all duplicate elements in a list
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
seen = set()
duplicates = set()

for n in numbers:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

print(duplicates)

# Find the most frequent number
numbers = [1, 3, 2, 3, 4, 3, 2]

freq = {}

for n in numbers:
    freq[n] = freq.get(n, 0) + 1

answer = max(freq, key=freq.get)
print(answer)

# Separate even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even:", even)
print("Odd:", odd)

# Merge two sorted lists
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

i = 0
j = 0
result = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

print(result)