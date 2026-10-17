from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        # Keep each number's original index, then sort by
        # (digit sum, number) as the problem requires.
        ordered = sorted(
            (digit_sum(num), num, i)
            for i, num in enumerate(nums)
        )

        # target_from[i] is the original index of the item
        # that belongs at sorted position i.
        target_from = [original_index for _, _, original_index in ordered]

        visited = [False] * len(nums)
        swaps = 0

        for start in range(len(nums)):
            if visited[start]:
                continue

            cycle_length = 0
            pos = start

            while not visited[pos]:
                visited[pos] = True
                cycle_length += 1
                pos = target_from[pos]

            if cycle_length > 1:
                swaps += cycle_length - 1

        return swaps