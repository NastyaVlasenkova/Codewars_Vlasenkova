'''
8 kyu
Name: Jenny's secret message
https://www.codewars.com/kata/55225023e1be1ec8bc000390
Task: Дженни написала функцию, которая возвращает приветствие для пользователя.
Тем не менее, она влюблена в Джонни и хотела бы приветствовать его немного по-другому.
Она добавила особый случай к своей функции, но допустила ошибку.
'''

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)