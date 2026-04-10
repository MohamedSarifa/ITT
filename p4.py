from itertools import count, islice

for n in islice(count(10), 5):
    print(n)