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