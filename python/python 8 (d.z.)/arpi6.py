import random
def openfile():
     with open('anna.csv', 'r', encoding = 'utf-8') as f:
         file = f.readlines()
         dictionary = {}
         for line in file:
             string = line.split(', ')
             string[1] = string[1].strip()
             dictionary[string[0]] = string[1]
         return dictionary

def guess():
    dictionary = openfile()
    arr = sorted(dictionary.keys())
    word = str(random.choice(arr))
    p = dictionary[word]
    print('Can you guess?. Help: '+p)
    i = 3
    while i != 0:
        i-=1
        t = input('Word: ')
        if t == word:
            print('You are right.')
            break
        else:
            if i == 0:
                print('You did not guess.', 'you have to say this.' +word)
                break
            t = print('You did not guess.' 'You have two attempts.' +str(i))
def main():
    guess()
    a = input('Did you like it, would you like to play again?')
    if a == ('yes' or 'no'):
        main()
    else:
        print('bye')
main()
