import re
def read(название):
    with open(название, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def text_to_sent(text):

    text_to = re.split('[.!?]', text)
    return text_to

def punct(text):
    te = [re.sub('[^\w\s]','', sent) for sent in text]
    return te

def len_aver(sent):
    for se in sent:
        words = se.split()
        if len(words) > 10:
            num = 0
            len_se = 0
            for word in words:
                num +=1
                len_se += len(word)
            if num != 0:
                len_aver = len_se/num
            print(se, ' - Это предложение со словами длины {:.2}'.format(len_aver))

def result(file_name):
    p = read(file_name)
    m = text_to_sent(p)
    n = punct(m)
    len_aver(n)

result('anna.txt')
