'''
6 kyu
Name: LOTTO 6 aus 49 - 6 of 49
https://www.codewars.com/kata/57a98e8172292d977b000079
Task: В Германии у нас есть "ЛОТО 6 aus 49". Это означает, что 6 из 49 чисел выпадают как выигрышная комбинация.
Существует также "Superzahl", дополнительный номер, который может увеличить вашу выигрышную категорию.
'''


import random
def number_generator():
    result=[]
    result+=sorted(random.sample(range(0,49),6))
    result+=random.sample(range(0,10),1)
    return result

def check_for_winning_category(your_numbers, winning_numbers):
    num = your_numbers[:len(your_numbers)-1]
    last_num=your_numbers[-1]
    win_num=winning_numbers[:len(your_numbers)-1]
    last_win_num=winning_numbers[-1]
    matches = 0
    for item in num:
        if item in win_num:
            matches+=1
    if matches <= 1 or (matches == 2 and last_win_num != last_num):
        return -1
    if last_win_num==last_num:
        return (7 - matches) * 2 -1
    else:
        return (7 - matches) * 2