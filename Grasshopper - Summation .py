'''
8 kyu
Name: Grasshopper - Summation
https://www.codewars.com/kata/55d24f55d7dd296eb9000030
Task: Напишите программу, которая находит суммирование каждого числа от 1 до num.
Число всегда будет положительным целым числом, большим 0.
'''

def summation(num):
    res=0
    for item in range (1,num+1):
        res+=item
    return res