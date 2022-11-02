'''
8 kyu
Name: Find the first non-consecutive number
https://www.codewars.com/kata/58f8a3a27a5c28d92e000144
Task: найти первый элемент массива, который не является последовательным.
'''

def first_non_consecutive(arr):
    for i in range(1,len(arr)):
        if (arr[i] - arr[i - 1] != 1):
            return arr[i]
    return None