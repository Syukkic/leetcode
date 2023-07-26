"""
https://leetcode.com/problems/merge-strings-alternately

You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.

"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_alphabet = []
        min_len = min(len(word1), len(word2))

        for idx in range(min_len):
            merged_alphabet.append(word1[idx])
            merged_alphabet.append(word2[idx])

        merged_alphabet.append(word1[min_len:])
        merged_alphabet.append(word2[min_len:])

        merged_word = "".join(merged_alphabet)
        return merged_word


s = Solution()
assert s.mergeAlternately("abc", "pqr") == "apbqcr"
assert s.mergeAlternately("ab", "pqrs") == "apbqrs"
assert s.mergeAlternately("abcd", "pq") == "apbqcd"
