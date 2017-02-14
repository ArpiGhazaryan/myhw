import re

with open('konrol2.txt', 'r', encoding='UTF-8') as f:
    f = f.read()
    lines = 0
    for line in f:
        lines += 1
result = str(lines)
open('arpijan.txt', 'w').write(result)
