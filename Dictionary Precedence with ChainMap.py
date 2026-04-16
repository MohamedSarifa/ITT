from collections import ChainMap
d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}
combined = ChainMap(d1, d2)
print(combined['b']) # Output: 10 (takes from first dict)
