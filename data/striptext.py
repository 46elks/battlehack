import re

with open('adjectives.txt') as f:
    for line in f:
        line = line.strip()
        if re.match("^[a-z]*$", line):
            print(line)
