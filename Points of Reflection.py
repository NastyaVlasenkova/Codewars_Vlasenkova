'''
8 kyu
Name: Points of Reflection
https://www.codewars.com/kata/57bfea4cb19505912900012c
Task: Учитывая две точки P и Q, выведите симметричную точку точки P относительно Q.
Каждый аргумент представляет собой двухэлементный массив целых чисел, представляющих координаты точки X и Y.
Выходные данные должны быть в том же формате, с указанием координат X и Y точки P1.
'''

def symmetric_point(p, q):
    return [2*q[0] - p[0], 2*q[1] - p[1]]