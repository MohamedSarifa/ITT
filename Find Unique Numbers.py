from collections import Counter
nums = [5, 3, 5, 2, 3, 1, 4, 1, 2]
counts = Counter(nums)
unique = [num for num, count in counts.items() if count == 1]
print(unique)
