'''
6 kyu
Name: Image host filename generator
https://www.codewars.com/kata/586a933fc66d187b6e00031a
Task: Необходимо создать функцию для генерации случайных и уникальных имен файлов изображений.
'''

from random import sample
def generateName():
    letters="abcdefghijklmnopqrstuvwxyz"
    while True:
        name = ''.join(sample(letters, 6))
        if not photoManager.nameExists(name):
            return name