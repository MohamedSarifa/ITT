s = "Hello 123"
vowels = "aeiouAEIOU"
v = sum(1 for c in s if c in vowels)
d = sum(1 for c in s if c.isdigit())
s_count = sum(1 for c in s if c.isspace())
c = sum(1 for c in s if c.isalpha() and c not in vowels)

print(f"Vowels: {v}\nConsonants: {c}\nDigits: {d}\nSpaces: {s_count}")
