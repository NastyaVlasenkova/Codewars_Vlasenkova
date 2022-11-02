'''
7 kyu
Name: Parts of a list
https://www.codewars.com/kata/56f3a1e899b386da78000732
Task: Напишите функцию, которая предоставляет все способы разделения списка (массива),
состоящего по крайней мере из двух элементов, на две непустые части.
'''

def partlist(arr):
    result=[]
    for item, elem in enumerate(arr):
        if item==len(arr)-1:
            break
        else:
            result.append((" ".join(arr[:item+1])," ".join(arr[item+1:])))
    return result