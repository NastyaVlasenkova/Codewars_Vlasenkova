'''
6 kyu
Name: Nearly Flatten a Messy Array
https://www.codewars.com/kata/5ae64f86783bb4722c0000d7
Task: Вам предоставляется массив произвольной глубины, который необходимо почти сгладить в 2-мерный массив.
Глубина данного массива также неоднородна, поэтому некоторые части могут быть глубже других.
'''


def near_flatten(nested):
    res = []
    for item in nested:
        if isinstance(item[0], int):
            res.append(item)
        else:
            res.extend(near_flatten(item))
    return sorted(res)