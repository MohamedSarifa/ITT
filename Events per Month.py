from collections import Counter
events = ["2025-01-10", "2025-01-20", "2025-02-05"]
months = [e[:7] for e in events]
print(Counter(months))
