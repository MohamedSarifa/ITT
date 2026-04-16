with open('file.txt', 'r') as f:
    lines = sorted(f.readlines())
    for line in lines:
        print(line.strip())
