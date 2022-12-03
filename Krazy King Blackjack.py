'''
5 kyu
Name: Krazy King Blackjack
https://www.codewars.com/kata/57bb798756449dea77000020
Task: Напишите функцию, которая вводит список строк (представляющих комбинацию для блэкджека)
и целое число, представляющее альтернативное значение короля.
Функция должна выводить целое число, представляющее значение комбинации, если оно меньше или равно 21,
и False, если оно превышает 21. За исключением альтернативного значения короля, применяются обычные правила блэкджека.
'''


dict={'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
def krazy_king_blackjack (hand, king_value):
    res=sum(dict[i] for i in hand)
    if res<=11 and "A" in hand and "K" not in hand:
        res+=10
    res2 = 0
    for i in hand:
        if i != "K":
            res2 += dict[i]
        else:
            res2 += king_value
    if res2<=11 and "A" in hand:
        res2+=10
    if res>21 and res2>21:
        return False
    elif res2 > 21:
        return res
    else:
        if res > 21:
            return res2
        else:
            return max(res, res2)