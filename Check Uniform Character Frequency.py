from collections import Counter
s = "aabbccddeeffgg"
counts = Counter(s)
print(len(set(counts.values())) == 1)
