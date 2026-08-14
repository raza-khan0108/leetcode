from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            
            # Shrink window if any character appears more than twice
            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1
            
            # Update max length
            max_len = max(max_len, right - left + 1)
            
        return max_len