'''
7 kyu
Name: Number climber
https://www.codewars.com/kata/559760bae64c31556c00006b
Task: Для каждого положительного целого числа N существует уникальная последовательность,
начинающаяся с 1 и заканчивающаяся на N и такая, что каждое число в последовательности является
либо удвоением предыдущего числа, либо удвоением плюс 1.
'''

def climb(n):
    result=list()
    while (n>=1):
        result.append(n)
        n=n//2
    return list(reversed(result))