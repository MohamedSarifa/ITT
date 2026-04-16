lines_seen = set()
with open('file.txt', 'r') as f:
    for line in f:
        if line not in lines_seen:
            print(line.strip())
            lines_seen.add(line)
