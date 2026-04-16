import re
from collections import Counter

with open('file.txt', 'r') as f:
    words = re.findall(r'\w+', f.read().lower())
    for word, count in Counter(words).items():
        print(f"{word}: {count}")
