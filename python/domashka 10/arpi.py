import re

with open('alla.html', 'r', encoding='utf-8') as f:
    f = f.read()

reg = 'Отряд.*?([А-Яа-я]+)'
r = re.search(reg, f, re.DOTALL)
res = r.group(1)
a = open('anna.txt', 'w', encoding='utf-8')
a.write(res)
a.close()


