"""
You are given an array of characters letters that is sorted in non-decreasing order,
and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters.
"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        print(left)
        print(left % len(letters))
        return letters[left % len(letters)]


case1, target1 = ["c", "f", "j"], "a"
case2, target2 = ["c", "f", "j"], "c"
case3, target3 = ["x", "x", "y", "y"], "z"
case4, target4 = ["c", "f", "j"], "j"
case5, target5 = ["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e"

s = Solution()

assert s.nextGreatestLetter(case1, target1) == "c"
# assert s.nextGreatestLetter(case2, target2) == "f"
# assert s.nextGreatestLetter(case3, target3) == "x"
# assert s.nextGreatestLetter(case4, target4) == "c"
# assert s.nextGreatestLetter(case5, target5) == "n"
