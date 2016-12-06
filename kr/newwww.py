f = open('control.txt', encoding='utf-8')
for line in f:
    len(line.split(' '))
    max_len = max(len(word) for word in line.split())
    if max_len < 10:
        print(line)
