from math import gcd
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        longest = 0

        for start in range(len(nums)):
            product = 1
            current_gcd = 0
            current_lcm = 1

            for end in range(start, len(nums)):
                number = nums[end]

                product *= number
                current_gcd = gcd(current_gcd, number)
                current_lcm = current_lcm * number // gcd(current_lcm, number)

                if product == current_gcd * current_lcm:
                    longest = max(longest, end - start + 1)

        return longest