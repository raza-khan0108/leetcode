from typing import List

class Solution:
    def minSumSquareDiff(
        self,
        nums1: List[int],
        nums2: List[int],
        k1: int,
        k2: int
    ) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        # If all differences can be reduced to zero, the answer is zero.
        if sum(diffs) <= k:
            return 0

        # Binary search for the largest level we can lower all differences to
        # using at most k operations.
        low, high = 0, max(diffs)

        while low < high:
            mid = (low + high) // 2
            needed = sum(max(0, d - mid) for d in diffs)

            if needed <= k:
                high = mid
            else:
                low = mid + 1

        level = low
        used = sum(max(0, d - level) for d in diffs)
        remaining = k - used

        # Lower each difference to at most `level`, then distribute any
        # remaining operations one at a time among values at that level.
        answer = sum(min(d, level) ** 2 for d in diffs)
        answer -= remaining * (2 * level - 1)

        return answer