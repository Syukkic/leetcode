"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


s = Solution()

case1, target1 = [-1, 0, 3, 5, 9, 12], 9
case2, target2 = [-1, 0, 3, 5, 9, 12], 2
case3, target3 = [5], 5
case4, target4 = [5], -5
case5, target5 = [2, 5], 5

assert s.search(case1, target1) == 4
assert s.search(case2, target2) == -1
assert s.search(case3, target3) == 0
assert s.search(case4, target4) == -1
assert s.search(case5, target5) == 1
