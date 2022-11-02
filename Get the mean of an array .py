'''
8 kyu
Name: Get the mean of an array
https://www.codewars.com/kata/563e320cee5dddcf77000158
Task: Возвращает среднее значение данного массива, округленное в меньшую сторону до ближайшего целого числа.
'''

def get_average(marks):
    return sum(marks) // len(marks)