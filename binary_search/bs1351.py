"""
Given a m x n matrix grid which is sorted in non-increasing order
both row-wise and column-wise, return the number of negative numbers in grid.
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        negative_count = 0
        row = rows - 1
        col = 0

        while row >= 0 and col < cols:
            if grid[row][col] < 0:
                negative_count += cols - col
                row -= 1
            else:
                col += 1
        return negative_count


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

s = Solution()
assert s.countNegatives(grid=grid) == 8
