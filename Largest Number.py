'''
5 kyu (замена задачи на LeetCode)
Name: Largest Number
https://leetcode.com/problems/largest-number/
Task: Учитывая список неотрицательных целых чисел nums, расположите их так,
чтобы они образовывали наибольшее число, и верните его.
Поскольку результат может быть очень большим, поэтому вам нужно вернуть строку вместо целого числа.
'''


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def partition(l, r):
            current = l
            while l < r:
                if nums[l] + nums[r] > nums[r] + nums[l]:
                    nums[l], nums[current] = nums[current], nums[l]
                    current += 1
                l += 1
            nums[r], nums[current] = nums[current], nums[r]
            return current

        def quicksort(l, r):
            if l >= r: return
            pivot = partition(l, r)
            quicksort(l, pivot - 1)
            quicksort(pivot + 1, r)

        nums = [str(i) for i in nums]
        quicksort(0, len(nums) - 1)
        return "".join(nums) if nums[0] != "0" else "0"
