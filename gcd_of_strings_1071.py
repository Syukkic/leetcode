"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""

"""
GCD: Euclidean algorithm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
"""
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        common_divisor_length = gcd(len1, len2)

        common_divisor = str1[:common_divisor_length]
        if (
            common_divisor * (len1 // common_divisor_length) == str1
            and common_divisor * (len2 // common_divisor_length) == str2
        ):
            return common_divisor
        return ''


assert Solution().gcdOfStrings('ABCABC', 'ABC') == 'ABC'
assert Solution().gcdOfStrings('ABABAB', 'AB') == 'AB'
assert Solution().gcdOfStrings('LEET', 'CODE') == ''
