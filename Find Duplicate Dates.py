from collections import Counter
dates = ["2026-03-10", "2026-03-10", "2026-03-11"]
duplicates = [d for d, count in Counter(dates).items() if count > 1]
print(duplicates)
