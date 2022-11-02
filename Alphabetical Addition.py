'''
7 kyu
Name: Alphabetical Addition
https://www.codewars.com/kata/5d50e3914861a500121e1958
Task: Ваша задача - сложить буквы в одну букву.
Функции будет присвоено переменное количество аргументов, каждый из которых представляет собой добавляемую букву.
'''

def add_letters(*letters):
    count=0
    alphabet=list(map(chr, range(97, 123)))
    for item in letters:
        count+=1+alphabet.index(item)
    if count==0:
        return 'z'
    if count>26:
        count=count%26
    return alphabet[count-1]