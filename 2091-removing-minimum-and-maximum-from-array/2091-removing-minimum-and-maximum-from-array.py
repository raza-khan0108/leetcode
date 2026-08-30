from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # Find indices of minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Order indices such that a <= b
        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)

        # 3 options:
        # 1. Both from front: b + 1
        # 2. Both from back: n - a
        # 3. From both ends: (a + 1) + (n - b)
        return min(b + 1, n - a, (a + 1) + (n - b))