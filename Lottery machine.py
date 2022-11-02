'''
7 kyu
Name: Lottery machine
https://www.codewars.com/kata/5832db03d5bafb7d96000107
Task: код должен отфильтровывать все буквы и возвращать уникальные целые числа в виде
строки в порядке их первого появления
'''

def lottery(s):
    res=''
    for item in s:
        if item.isdigit():
            if item not in res:
                res+=item
    if res=='':
        return "One more run!"
    return res