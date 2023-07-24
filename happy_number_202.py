"""
https://leetcode.com/problems/happy-number/description/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    - Starting with any positive integer, 
        replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), 
        or it loops endlessly in a cycle which does not include 1.
    - Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""


class Solution:
    def if_happy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.calculate_sum_of_squares(n)
        return n == 1

    def calculate_sum_of_squares(self, num):
        sum_of_squares = 0
        while num > 0:
            digit = num % 10
            sum_of_squares += digit * digit
            num //= 10
        return sum_of_squares


s = Solution()

assert s.if_happy(19) is True
assert s.if_happy(2) is False
