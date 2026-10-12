class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        chosen = [0] * k

        # Each operation preserves how many times each bit occurs across
        # the array. Put each bit into as many of the k chosen values as possible.
        for bit in range(31):
            count = sum((num >> bit) & 1 for num in nums)

            for i in range(min(count, k)):
                chosen[i] |= 1 << bit

        return sum(x * x for x in chosen) % MOD