def count_tf(word, text): 
    return text.count(word) / len(text)
def count_df(word, texts): 
                            
    n = [1 for text in texts if word in text]
    
    return sum(n)
def count_idf(word, texts): 
    n = len(texts) / (1 + count_df(word, texts)) 
                                                
    return n
from math import log 
                    
                        
def count_tfidf(word, text, texts):
    tf = count_tf(word, text)
    idf = count_idf(word, texts)
    return log(tf, 10) * log(idf, 10)

import re

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

texts_dic = {}
for root, dirs, files in os.walk('D:\\wikipedia'):
    for f in files[:50]:
        with open(os.path.join(root, f), 'r', encoding='utf-8') as t:
            text = preprocessing(t.read())
            texts_dic[f.split('.')[0]] = text
texts = list(texts_dic.values())
for text in texts_dic:
    print("Top words in document {}".format(text)) 
    scores = {}
    for word in texts_dic[text]:
        scores[word] =  count_tfidf(word, texts_dic[text], texts)
    sorted_words = sorted(scores.items(), key=lambda x: x[1])
    for word, score in sorted_words[:5]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
