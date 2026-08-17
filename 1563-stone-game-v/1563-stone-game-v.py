from bisect import bisect_right
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0
        
        # 1-indexed prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        # dp[i][j]: max score for subarray [i..j]
        dp = [[0] * n for _ in range(n)]
        
        # maxL[i][j] = max_{k=i..j} (sum(i..k) + dp[i][k])
        # maxR[i][j] = max_{k=i..j} (sum(k..j) + dp[k][j])
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]
        
        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]
            
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]
                
                # Find largest split point mid (i <= mid < j) where left_sum <= total / 2
                # prefix[mid + 1] <= prefix[i] + total // 2
                target = prefix[i] + total // 2
                idx = bisect_right(prefix, target, i + 1, j + 1)
                mid = idx - 2  # 0-indexed split index
                
                res = 0
                
                # Case 1: left_sum == right_sum
                if mid >= i and (prefix[mid + 1] - prefix[i]) * 2 == total:
                    # Exactly half-split
                    res = max(
                        (prefix[mid + 1] - prefix[i]) + max(dp[i][mid], dp[mid + 1][j]),
                        maxL[i][mid - 1] if mid - 1 >= i else 0,
                        maxR[mid + 2][j] if mid + 2 <= j else 0
                    )
                else:
                    # Case 2: left_sum < right_sum for k <= mid
                    opt_left = maxL[i][mid] if mid >= i else 0
                    # Case 3: left_sum > right_sum for k >= mid + 1
                    opt_right = maxR[mid + 2][j] if mid + 2 <= j else 0
                    res = max(opt_left, opt_right)
                    
                dp[i][j] = res
                maxL[i][j] = max(maxL[i][j - 1], res + total)
                maxR[i][j] = max(maxR[i + 1][j], res + total)
                
        return dp[0][n - 1]