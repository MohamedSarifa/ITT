from collections import OrderedDict
s = "swiss"
counts = OrderedDict()
for char in s:
    counts[char] = counts.get(char, 0) + 1
for char, count in counts.items():
    if count == 1:
        print(char)
        break
