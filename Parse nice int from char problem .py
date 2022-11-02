'''
8 kyu
Name: Parse nice int from char problem
https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1
Task: Вы спрашиваете маленькую девочку: "Сколько тебе лет?" Она всегда говорит: "x лет".
Напишите программу, которая возвращает возраст девушки (0-9) в виде целого числа.
'''

def get_age(age):
    return int(age[0])