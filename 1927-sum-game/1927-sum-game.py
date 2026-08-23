class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum_l = sum_r = 0
        q_l = q_r = 0
        
        for i in range(half):
            if num[i] == '?':
                q_l += 1
            else:
                sum_l += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                q_r += 1
            else:
                sum_r += int(num[i])
                
        # Bob wins if and only if the balance equation holds
        # (sum_l - sum_r) == (q_r - q_l) / 2 * 9
        # Which is equivalent to: (sum_l - sum_r) * 2 == (q_r - q_l) * 9
        return (sum_l - sum_r) * 2 != (q_r - q_l) * 9