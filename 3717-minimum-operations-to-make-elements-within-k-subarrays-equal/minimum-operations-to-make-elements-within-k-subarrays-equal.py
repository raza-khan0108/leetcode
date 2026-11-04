from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Compress values so the Fenwick tree can index them.
        values = sorted(set(nums))
        rank = {value: i + 1 for i, value in enumerate(values)}

        class Fenwick:
            def __init__(self, size: int):
                self.tree = [0] * (size + 1)

            def add(self, index: int, amount: int) -> None:
                while index < len(self.tree):
                    self.tree[index] += amount
                    index += index & -index

            def prefix_sum(self, index: int) -> int:
                total = 0
                while index > 0:
                    total += self.tree[index]
                    index -= index & -index
                return total

            def kth(self, order: int) -> int:
                # Find the smallest index whose prefix sum is >= order.
                index = 0
                step = 1 << (len(self.tree).bit_length() - 1)

                while step:
                    next_index = index + step
                    if next_index < len(self.tree) and self.tree[next_index] < order:
                        index = next_index
                        order -= self.tree[next_index]
                    step >>= 1

                return index + 1

        counts = Fenwick(len(values))
        sums = Fenwick(len(values))
        window_sum = 0
        window_cost = [0] * (n - x + 1)

        # Calculate the cost for every length-x window.
        for right, number in enumerate(nums):
            index = rank[number]
            counts.add(index, 1)
            sums.add(index, number)
            window_sum += number

            if right >= x:
                old_number = nums[right - x]
                old_index = rank[old_number]
                counts.add(old_index, -1)
                sums.add(old_index, -old_number)
                window_sum -= old_number

            if right >= x - 1:
                start = right - x + 1

                # Either middle value is a median when x is even.
                median_index = counts.kth((x + 1) // 2)
                median = values[median_index - 1]

                left_count = counts.prefix_sum(median_index)
                left_sum = sums.prefix_sum(median_index)
                right_count = x - left_count
                right_sum = window_sum - left_sum

                window_cost[start] = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

        infinity = float("inf")

        # With zero chosen subarrays, every prefix has cost zero.
        previous = [0] * (n + 1)

        for count in range(1, k + 1):
            current = [infinity] * (n + 1)

            for end in range(1, n + 1):
                # Skip nums[end - 1].
                current[end] = current[end - 1]

                # Or choose the length-x window ending at end - 1.
                if end >= x and previous[end - x] != infinity:
                    start = end - x
                    current[end] = min(
                        current[end],
                        previous[end - x] + window_cost[start]
                    )

            previous = current

        return previous[n]