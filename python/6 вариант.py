def normaltext(text):
    arr = []
    for i in range(len(text)):
        word = text[i].strip('.,?()"')
        arr.append(word.lower())

    return arr
def openfile():
    with open(input('Название файла'), 'r', encoding='utf-8') as f:
         text = f.read()
         text = text.split()
    return text
def findomni(text):
     omniwords = []
     for i in range(len(text)):
         if len(text[i]) > 5:
             if text[i][:5] == 'omni':
                 omniwords.append(text[i])
     return omniwords
def biteomni(omniwords):
    words = []
    for i in range(len(omniwords)):
         words.append(omniwords[i].strip('omni'))
    return words
def unique(a):
    
    uniquearr = []
    for i in range(len(a)):
        if a[i] not in uniquearr:
            uniquearr.append(a[i])
    return uniquearr
def countfreq(words, text):
    q = len(text)
    uniqwords = unique(words)
    result = []
    for i in range(len(uniqwords)):
        a = words.count(uniqwords[i])
        if a != 0:
            result.append(uniqwords[i]+': частота - '+ str((a/q)*100) + '%')
        else:
            result.append(uniqwords[i]+' Оно встречаются ')
    return result
def  sum_up(resultomni, resultwords):
    for i in range(len(resultomni)):
        print(resultation[i])
        print(resulwords[i])
def main():
    text = normaltext(openfile())
    omniwords = guessomni(text)
    words = biteomni(omniwords)
    consequencewords = countfrequency(words, text)
    consequencetomni = countfrequency(omniwords, text)
    sum_up(resultomni, consequencetwords)
main()
