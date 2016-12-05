score = 0
count = 0
with open ('Anna.txt', 'r', encoding='utf-8') as f:
    for line in f:
        string = line.split()
        count += len(string)
        for word in string:
            if word[0].istitle():
                    score +=1
if count == 0:
    print('Ничего не найдено( Нечего нету!')
else:
    total = score/count*100
    print('Количество заглавных букв составляет: ', total, '%', sep ='')
