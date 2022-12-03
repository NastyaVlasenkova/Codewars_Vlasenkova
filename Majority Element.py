'''
5 kyu (замена задачи на LeetCode)
Name: Majority Element
https://leetcode.com/problems/majority-element/
Task: Учитывая массив nums размера n, верните элемент большинства.
Мажоритарный элемент - это элемент, который появляется более ⌊n / 2⌋ раз.
Вы можете предположить, что элемент большинства всегда существует в массиве.
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=count=0
        for item in nums:
            if count==0:
                res=item
            if item==res:
                count+=1
            else:
                count-=1
        return res