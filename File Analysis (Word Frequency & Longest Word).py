try:
   with open("input.txt", "r", encoding="utf-8", errors="ignore") as infile:
        paragraph = infile.read()
except FileNotFoundError:
    paragraph = ""

words = []
current_word = ""
for char in paragraph:
    if char.isalnum():
        current_word += char.lower()
    else:
        if current_word:
            words.append(current_word)
            current_word = ""
if current_word:
    words.append(current_word)

word_freq = {}
for w in words:
    word_freq[w] = word_freq.get(w, 0) + 1

longest_word = ""
if words:
    for w in words:
        if len(w) > len(longest_word):
            longest_word = w

reversed_word = longest_word[::-1]

output_lines = ["Repeated Words:"]
for w, count in word_freq.items():
    if count > 1:
        output_lines.append(f"{w} : {count}")

output_lines.append(f"\nLongest word: {longest_word}")
output_lines.append(f"Reversed longest word: {reversed_word}")

with open("output.txt", "w") as outfile:
    outfile.write("\n".join(output_lines))
