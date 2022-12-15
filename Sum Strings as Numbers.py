'''
4 kyu
Name: Sum Strings as Numbers
https://www.codewars.com/kata/5324945e2ece5e1f32000370
Task: Учитывая строковые представления двух целых чисел, верните строковое представление суммы этих целых чисел.
Ваше решение должно работать с огромными числами (около миллиона цифр), преобразование в int не будет работать.
'''


def sum_strings(s1, s2):

    if s1 == "" and s2 == "":
        return "0"
    elif s1 == "":
        return s2
    elif s2 == "":
        return s1
    result = ['0'] * max(len(s1), len(s2))
    i, j, k = len(s1) - 1, len(s2) - 1, len(result) - 1
    carry = 0
    while i >= 0 or j >= 0:
        x = int(s1[i]) if i >= 0 else 0
        y = int(s2[j]) if j >= 0 else 0
        digit_sum = x + y + carry
        carry = digit_sum // 10
        result[k] = str(digit_sum % 10)
        i -= 1
        j -= 1
        k -= 1
    if carry > 0:
        result.insert(0, str(carry))
    if len(result) == 1 and result[0] == "0":
        result == "0"
    elif result[0] == "0":
        result[0] = ""
    return ''.join(result)