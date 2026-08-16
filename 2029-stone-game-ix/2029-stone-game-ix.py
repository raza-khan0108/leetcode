class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt = [0, 0, 0]
        for s in stones:
            cnt[s % 3] += 1
        
        c0, c1, c2 = cnt[0], cnt[1], cnt[2]
        
        # If the number of 0-modulo stones is even, they do not change the turn parity.
        # Alice wins if and only if both 1-modulo and 2-modulo stones are available.
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        
        # If the number of 0-modulo stones is odd, the turn parity flips after 0s are consumed.
        # Alice wins if and only if the difference between 1s and 2s is greater than 2.
        return abs(c1 - c2) > 2