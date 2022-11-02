'''
8 kyu
Name: Are You Playing Banjo?
https://www.codewars.com/kata/53af2b8861023f1d88000832
Task: Создайте функцию, которая отвечает на вопрос "Вы играете на банджо?".
Если ваше имя начинается с буквы "R" или строчной буквы "r", вы играете на банджо!
'''

def are_you_playing_banjo(name):
    if name[0]=="R" or name[0]=="r":
        name+=' plays banjo'
    else:
        name+=' does not play banjo'
    return name