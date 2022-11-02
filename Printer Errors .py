'''
7 kyu
Name: Printer Errors
https://www.codewars.com/kata/56541980fa08ab47a0000040
Task: по заданной строке вернет частоту ошибок принтера в виде строки, представляющей рациональное число,
числителем которого является количество ошибок, а знаменателем - длина управляющей строки.
'''

def printer_error(s):
    n_error=0
    for item in s:
        if not 'a'<=item<='m':
            n_error+=1
    return f'{n_error}/{len(s)}'