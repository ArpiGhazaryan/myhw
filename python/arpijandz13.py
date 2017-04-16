import re
import os
punct = '[.!;_,-]'

def num_files(search):
    files = [r for r in os.listdir('.') if os.path.isfile(r) and len(re.findall(search, r))>1] 
    return files

def files_only(files):
    names = [i.rsplit('.', 1)[0] for i in files]
    return names

def result(search):
    f = num_files(search)
    n = files_only(f)
    print(len(f), ', '.join(f))
    print(', '.join(set(n)))

result(punct)

