from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        blocks = deque()  # Indices of the maximum blocks
        right = n - 1
        cost = 0
        answer = 0

        for left in range(n - 1, -1, -1):
            value = nums[left]

            # Merge smaller blocks into this new, larger value.
            while blocks and nums[blocks[-1]] <= value:
                index = blocks.pop()
                end = blocks[-1] if blocks else right + 1
                cost += (end - index) * (value - nums[index])

            blocks.append(left)

            # Remove elements from the right until the cost is within k.
            while cost > k:
                cost -= nums[blocks[0]] - nums[right]

                if blocks[0] == right:
                    blocks.popleft()

                right -= 1

            # Count valid subarrays that start at left.
            answer += right - left + 1

        return answer