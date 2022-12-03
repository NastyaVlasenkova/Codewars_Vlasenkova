'''
6 kyu
Name: Find The Parity Outlier
https://www.codewars.com/kata/5526fc09a1bbd946250002dc
Task: Вам предоставляется массив (который будет иметь длину не менее 3, но может быть очень большим),
содержащий целые числа.
Массив либо полностью состоит из нечетных целых чисел, либо полностью состоит из четных целых чисел,
за исключением одного целого N числа .
Напишите метод, который принимает массив в качестве аргумента и возвращает этот "выброс" N.
'''

def find_outlier(integers):
    odd=[]
    even=[]
    for i in integers:
        if i%2==1:
            odd.append(i)
        elif i%2==0:
            even.append(i)
    if len(even)>len(odd):
        return odd[0]
    else:
        return even[0]