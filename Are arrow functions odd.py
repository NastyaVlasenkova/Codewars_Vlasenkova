'''
8 kyu
Name: Are arrow functions odd?
https://www.codewars.com/kata/559f80b87fa8512e3e0000f5
Task: вернуть массив без четных значений
'''

odds = lambda arr: [x for x in arr if x % 2 == 1]