
import re
from math import log

punct = '[*.,!«»1234567890?&@"$\[\]\(\):;%#&\'—-]'

f_words = open('D:\\file.txt', 'r', encoding='utf-8').read() 
func_words = f_words.strip().split()


def preprocessing(text): 
    text_wo = re.sub(punct, '', text.lower())    
    words = text_wo.strip().split() 
    words_w_funcwords = [] 
    for w in words:
        if w not in func_words and len(w) > 3: 
            words_w_funcwords.append(w)     
           
    return words_w_funcwords
import os 
anek = ''
teh = ''
izvest = ''
for root, dirs, files in os.walk('D:\\texts'): 
    for f in files:
        if 'anekdots' in root:
            num_anek = len(files)
            anek += open(os.path.join(root, f), 'r', encoding='utf-8').read()
            
        elif 'izvest' in root:
            num_izvest = len(files)
            izvest += open(os.path.join(root, f),'r', encoding='utf-8').read()
        elif 'teh_mol' in root:
            num_teh = len(files)
            teh += open(os.path.join(root, f),'r', encoding='utf-8').read()
            
words_anek = preprocessing(anek) 
words_teh = preprocessing(teh)
words_izvest = preprocessing(izvest)


words = words_anek + words_teh + words_izvest 
def freq_dict(arr): 
    dic = {}
    for element in arr:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1      
        
    return dic
def create_bigram(arr):
    bigrams = [] 
    for i in range(1, len(arr) - 1):
        a = arr[i-1] + ' ' + arr[i]
        bigrams.append(a)
    return bigrams
bigram_anek = create_bigram(words_anek)
bigram_teh = create_bigram(words_teh)
bigram_izvest = create_bigram(words_izvest)
bigrams = create_bigram(words)

bigram_anek_freq = freq_dict(bigram_anek) 
bigram_izvest_freq = freq_dict(bigram_teh)
bigram_teh_freq = freq_dict(bigram_izvest)
bigrams_freq=freq_dict(bigrams)
def pmi_for_cats(x, y):
    if y == 'anek':
        dic = bigram_anek_freq
        arr = bigram_anek
        num = len(bigram_anek)
        
        с1_freq = bigram_izvest_freq
        с2_freq = bigram_teh_freq 
     
    elif y == 'teh':
        dic = bigram_teh_freq
        arr = bigram_teh
        num = len(bigram_teh)
        
        с1_freq=  bigram_izvest_freq
        с2_freq= bigram_anek_freq
        
       
    elif y == 'izvest':
        dic = bigram_izvest_freq
        arr = bigram_izvest
        num = len(bigram_izvest)
        
        с1_freq = bigram_anek_freq 
        с2_freq = bigram_teh_freq

       
    p_xy = dic[x]/len(arr) 
    p_x, p_y = (с1_freq[x] + с2_freq[x])/(len(с1_freq)+len(с2_freq)), num/(len(bigrams)) 
                                                
    pmi = log(p_xy/(p_x * p_y)) 

    return pmi
at_pmi = {}
i = 0


for word in sorted(bigrams_freq, key = lambda m: -bigrams_freq[m]): 
                                                                    
    if i > 100:
        break
    try:
        pmi_anek = pmi_for_cats(word, 'anek') 
       
    except KeyError: 
        pmi_anek = 0
    try:
        pmi_teh = pmi_for_cats(word, 'teh')
    except KeyError:
        pmi_teh = 0
    try:
        pmi_izvest = pmi_for_cats(word, 'izvest')
    except KeyError:
        pmi_izvest = 0
    max_pmi = max(pmi_anek, pmi_teh, pmi_izvest) 
    if max_pmi == 0:
        continue
    if max_pmi == pmi_anek: 
        cat = 'anek'
    elif max_pmi == pmi_teh:
        cat = 'teh'
    elif max_pmi == pmi_izvest:
        cat = 'izvest'
    print(word, cat) 
    i += 1
