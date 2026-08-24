from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Precompute prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
            
        # Base case: at the last index, the player takes the whole prefix
        dp = prefix[-1]
        
        # Iterate backwards from n - 2 down to 1
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
            
        return dp