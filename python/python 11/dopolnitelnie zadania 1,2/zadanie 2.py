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
def create_bigram(arr):
    bigrams = [] 
    for i in range(1, len(arr) - 1):
        a = arr[i-1] + ' ' + arr[i]
        bigrams.append(a)
    return bigrams

def freq_dict(arr): 
    dic = {}
    for element in arr:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1      
        
    return dic

def count_pmi(x, y): 
    p_xy = bigram_freq[' '.join([x, y])]/len(bigrams) 
    p_x, p_y = word_freq[x]/len(words), word_freq[y]/len(words) 
    pmi = log(p_xy/(p_x * p_y))
    return pmi
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
            
    bigrams = create_bigram(words_w_funcwords)

    return bigrams, words_w_funcwords
import os

bigrams_dic = {}
words_dic = {}
for root, dirs, files in os.walk('D:\\wikipedia'):
    
    for f in files[:50]:
        with open(os.path.join(root, f), 'r', encoding='utf-8') as t:
            bigram, words = preprocessing(t.read())
            bigrams_dic[f.split('.')[0]] = bigram
            words_dic[f.split('.')[0]] = words
texts = list(bigrams_dic.values())
for text_name in bigrams_dic: 
    print("Top bigrams in document {}".format(text_name))
    
    scores_tf_idf= {} 
    scores_pmi= {} 
    
    bigram_freq = freq_dict(bigrams_dic[text_name])  
    word_freq = freq_dict(words_dic[text_name]) 
    
    for bigram in bigrams_dic[text_name]:
        bigrams = bigrams_dic[text_name]
        scores_tf_idf[bigram] =  count_tfidf(bigram, bigrams_dic[text_name], texts)
        x,y = bigram.split()
        scores_pmi[bigram] = count_pmi(x,y) 
        
    score_idf_pmi = {} 
    i = 0    
    for bigrm_pmi in sorted(scores_pmi, key=lambda x: -scores_pmi[x]):  
                                                       
        if i > 9:
            break
        score_idf_pmi[bigrm_pmi] = scores_tf_idf[bigrm_pmi]                 
        i += 1
   
    i = 0
    for bigrm_pmi in sorted(score_idf_pmi, key=lambda x: score_idf_pmi[x]):  

                                                        
        if i > 4:
            break    
        print("\tBigram: {:>35}, TF-IDF: {}, PMI: {}".format(bigrm_pmi, round(score_idf_pmi[bigrm_pmi],5), round(scores_pmi[bigrm_pmi],5)))
        i += 1
        
