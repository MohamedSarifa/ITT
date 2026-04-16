text = "Python is powerful and easy"
words = text.split()
print(f"Longest: {max(words, key=len)}")
print(f"Shortest: {min(words, key=len)}")
