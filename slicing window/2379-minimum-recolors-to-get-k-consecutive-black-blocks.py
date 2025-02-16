# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        white_count = blocks[:k].count('W')
        min_recolors = white_count

        if min_recolors == 0:
            return 0

        for i in range(1, n - k + 1):
            if blocks[i - 1] == 'W':
                white_count -= 1
            if blocks[i + k - 1] == 'W':
                white_count += 1

            min_recolors = min(min_recolors, white_count)

        return min_recolors
