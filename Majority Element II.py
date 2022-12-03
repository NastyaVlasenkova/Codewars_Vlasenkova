'''
5 kyu (замена задачи на LeetCode)
Name: Majority Element II
https://leetcode.com/problems/majority-element-ii/
Task: Учитывая массив nums размера n, верните элемент большинства.
Мажоритарный элемент - это элемент, который появляется более ⌊n / 3⌋ раз.
Вы можете предположить, что элемент большинства всегда существует в массиве.
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                candidate1 = n
            elif count2 == 0:
                count2 = 1
                candidate2 = n
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]
