from itertools import combinations_with_replacement

items = [1, 2]
for combo in combinations_with_replacement(items, 2):
    print(combo)