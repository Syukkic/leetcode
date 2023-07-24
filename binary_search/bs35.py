"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = left + 1
            else:
                right = right - 1

        if nums[mid] > target:
            return mid
        else:
            return mid + 1


case1, target1 = [1, 3, 5, 6], 5
case2, target2 = [1, 3, 5, 6], 2
case3, target3 = [1, 3, 5, 6], 7

s = Solution()

assert s.searchInsert(case1, target1) == 2
assert s.searchInsert(case2, target2) == 1
assert s.searchInsert(case3, target3) == 4
