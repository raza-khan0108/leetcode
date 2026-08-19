import collections
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Dictionary to store the bitmask of reserved seats for each row
        seats = collections.defaultdict(int)
        
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                seats[r] |= (1 << c)
        
        # Assume max capacity initially (2 families per row)
        ans = 2 * n
        
        # Check only the rows that have reservations
        for mask in seats.values():
            ans -= 2 # Deduct the initially assumed 2 families for this row
            
            # If both left and right blocks are free
            if not (mask & 60) and not (mask & 960):
                ans += 2
            # If at least one of the left, right, or middle blocks is free
            elif not (mask & 60) or not (mask & 960) or not (mask & 240):
                ans += 1
                
        return ans