'''
6 kyu (замена задачи на LeetCode)
Name: Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Task: Учитывая строку, содержащую цифры от 2-9 включительно, верните все возможные комбинации букв,
которые может представлять число. Верните ответ в любом порядке.
'''


class Solution(object):
    def letterCombinations(self,digits):
        L = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def combinations(i, current):
            if i == len(digits):
                if len(current) > 0:
                    result.append(''.join(current))
                return
            for item in L[digits[i]]:
                current.append(item)
                combinations(i + 1, current)
                current.pop()

        combinations(0, [])

        return result