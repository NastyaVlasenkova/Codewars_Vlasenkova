'''
5 kyu
Name: Number of trailing zeros of N!
https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
Task: Напишите программу, которая вычислит количество конечных нулей в факториале заданного числа.
Вы не должны вычислять факториал. Найдите другой способ найти количество нулей.
'''


def zeros(n):
    zero = 0
    while n >= 5:
        n = n//5
        zero+=n
    return zero