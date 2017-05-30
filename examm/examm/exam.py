#задание 1
import re
punct = '[*,!«»1234567890?&@"$\[\]\(\):;/%#&\'—-]'

def prep(text): # функция предобработки текста (берем из прошлого дз)
    text_wo = re.sub(punct, '', text) # удаляем пунктуацию   

    return text_wo
f_words = open('D:\\s.txt', 'r', encoding='utf-8').read() #читаем статью из файла 
 
func_words = f_words.strip().split()

bigrams = [] # будем собирать пары слов и далее их обрабатывать
for i in range(1, len(func_words) - 1):
    bigrams.append(' '.join([func_words[i - 1], func_words[i]]))

name_fam = [prep(b) for b in bigrams if re.search('^[А-Я]\. [А-Я][^\s\d\.\,]+', b)]
print(name_fam)

#задание 2

name_fam1 = [prep(b) for b in bigrams if re.search('^[А-Я][а-я]+ [А-Я][а-я]', b)]

bigramss = [] # будем собирать для формала А. Ф. Иванов по 3 слова и далее их обрабатывать
for i in range(2, len(func_words) - 1):
    bigramss.append(' '.join([func_words[i - 2],func_words[i - 1], func_words[i]]))

name_fam2 = [prep(b) for b in bigramss if re.search('^[А-Я]\. [А-Я]\. [А-Я][^\s\d\.\,]+', b)]
print(name_fam1)
print(name_fam2)
