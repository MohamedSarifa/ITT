from itertools import combinations

items = ['A', 'B', 'C', 'D']
for combo in combinations(items, 2):
    print(combo)