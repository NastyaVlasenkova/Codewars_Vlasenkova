'''
5 kyu (замена задачи на LeetCode)
Name: Partition Array According to Given Pivot
https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
Task: Вам дается целочисленный массив с индексом 0 и целое число .
Измените порядок таким образом, чтобы были выполнены следующие условия:
Каждый элемент, меньший, чем, появляется перед каждым элементом, большим, чем .pivot
Каждый элемент, равный , появляется между элементами меньше и больше , чем .pivot
'''


class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        return [item for item in nums if item < pivot] +[item for item in nums if item == pivot] + \
        [item for item in nums if item > pivot]