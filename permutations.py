from itertools import permutations

s = '123'
for p in permutations(s):
    print(''.join(p))