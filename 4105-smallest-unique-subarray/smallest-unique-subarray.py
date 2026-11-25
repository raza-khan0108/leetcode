from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod1, mod2 = 1_000_000_007, 1_000_000_009
        base = 911_382_323

        # Prefix hashes and powers, for two moduli.
        prefix1 = [0] * (n + 1)
        prefix2 = [0] * (n + 1)
        power1 = [1] * (n + 1)
        power2 = [1] * (n + 1)

        for i, value in enumerate(nums):
            prefix1[i + 1] = (prefix1[i] * base + value) % mod1
            prefix2[i + 1] = (prefix2[i] * base + value) % mod2
            power1[i + 1] = (power1[i] * base) % mod1
            power2[i + 1] = (power2[i] * base) % mod2

        def has_unique_subarray(length: int) -> bool:
            counts = {}

            for start in range(n - length + 1):
                end = start + length

                hash1 = (prefix1[end] - prefix1[start] * power1[length]) % mod1
                hash2 = (prefix2[end] - prefix2[start] * power2[length]) % mod2
                key = (hash1, hash2)

                counts[key] = counts.get(key, 0) + 1

            return any(count == 1 for count in counts.values())

        low, high = 1, n

        while low < high:
            mid = (low + high) // 2

            if has_unique_subarray(mid):
                high = mid
            else:
                low = mid + 1

        return low