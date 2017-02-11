import re

with open('finlandia.html', 'r', encoding='utf-8') as f:
    html = f.read()
    html = re.sub('Финлянди', 'Малайзи', html, flags=re.I | re.DOTALL)

with open('arpijanmernemsrtit.txt', 'w', encoding='utf-8') as a:
    a = a.write(html)
