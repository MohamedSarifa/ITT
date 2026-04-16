paragraph="The sun rose slowly over the mountain peak, casting a golden glow across the valley below. In the valley, every tree and every flower seemed to wake up at once. The golden sun made the dew on the grass sparkle like tiny diamonds. It was a beautiful morning, and the valley felt peaceful as the sun continued to rise higher"

words = []
current_word = ""
for char in paragraph:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
        if 'A' <= char <= 'Z':
            current_word += chr(ord(char) + 32)
        else:
            current_word += char
    else:
        if current_word != "":
            words.append(current_word)
            current_word = ""
if current_word != "":
    words.append(current_word)

word_freq = {}
for w in words:
    if w in word_freq:
        word_freq[w] += 1
    else:
        word_freq[w] = 1

print("\nRepeated Words:")
for w in word_freq:
    if word_freq[w] > 1:
        print(w, ":", word_freq[w])

longest_word = ""
for w in words:
    if len(w) > len(longest_word):
        longest_word = w

reversed_word = ""
for i in range(len(longest_word) - 1, -1, -1):
    reversed_word += longest_word[i]

print("\nLongest word:", longest_word)
print("Reversed longest word:", reversed_word)
