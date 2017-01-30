import re 

def extract(): 
    f = open('anna.txt', 'r', encoding='utf-8') 
    text = f.read().strip() 
    f.close() 
    words = text.split() 
    for i in range(len(words)): 
        words[i] = words[i].lower().strip(';.,^()[]?!:') 
    return words 

def check(words): 
    forms = [] 
    for word in words: 
        regword = re.match ("загру(ж(у(сь)?|е(н(н(ая|о(е|й|го|му?)?|ы(х|е|й|ми?)|ую)?|[ыао]?|)))|з(ят(ся)?|и(те?(с[ья])?|шь(ся)?|л(ся|(а|о|и)(сь)?)?|м(ся)?|в(ш(и(х|ми?|й|е)?(с[ья])?|ую(ся)?|е(го|й|е|му?)(ся)?|ая?(ся)?)?)?)?))", word) 
        if regword != None and word not in forms:
            forms.append(word) 
    for word in forms:
        print(word)

check(extract())
