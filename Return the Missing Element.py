'''
7 kyu
Name: Return the Missing Element
https://www.codewars.com/kata/5299413901337c637e000004
Task: Напишите функцию, которая принимает последовательность уникальных целых чисел от 0 до 9 (включительно)
и возвращает недостающий элемент.
'''

def get_missing_element(seq):
    all=[0,1,2,3,4,5,6,7,8,9]
    for item in all:
        if item not in seq:
            return item