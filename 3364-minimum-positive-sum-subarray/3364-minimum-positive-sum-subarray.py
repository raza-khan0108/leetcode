from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # prefix[i] is the sum of nums before index i
        prefix = [0]
        for number in nums:
            prefix.append(prefix[-1] + number)

        smallest_positive = float("inf")
        n = len(nums)

        for start in range(n):
            for length in range(l, r + 1):
                end = start + length

                if end > n:
                    break

                # Sum of nums[start:end]
                subarray_sum = prefix[end] - prefix[start]

                if 0 < subarray_sum < smallest_positive:
                    smallest_positive = subarray_sum

        if smallest_positive == float("inf"):
            return -1

        return smallest_positive