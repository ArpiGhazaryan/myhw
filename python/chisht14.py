import os

def countdirs(path):
    counter = 0
    for root, dirs, files in os.walk(path):
        num = [file for file in files if file.endswith('.') == True]
        for file in num:
            files.pop(file)
        dictionary = {f[-1:-3]:' ' for f in files}
        if len(dictionary)+len(num) != len(files):
            counter +=1   
    print(counter)

def main():
    countdirs('.')

main()
