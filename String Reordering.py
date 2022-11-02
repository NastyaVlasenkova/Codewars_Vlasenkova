'''
7 kyu
Name: String Reordering
https://www.codewars.com/kata/5b047875de4c7f9af800011b
Task: Вводом будет массив словарей.
Возвращает значения в виде предложения, разделенного строками,
в порядке целочисленного эквивалента их ключей (в порядке возрастания).
'''

def sentence(List):
    result = dict()
    for item in List:
        result.update(item)
    sorted_result = sorted(result.keys(), key=int)
    result_string = ""
    for item in sorted_result:
        result_string +=(result.get(item)) + " "
    result_string = result_string.strip()
    return result_string