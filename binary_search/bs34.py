"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def find_leftmost(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                result = mid

        return result

    def find_rightmost(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = right - 1

            if nums[mid] == target:
                result = mid

        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_leftmost(nums, target)
        if left == -1:
            return [-1, -1]

        right = self.find_rightmost(nums, target)
        return [left, right]
