from collections import Counter
from typing import List

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        freq = Counter(s)
        
        # Check palindrome feasibility
        odd_char = ""
        odd_count = 0
        half_counts = {}
        
        for ch, count in freq.items():
            if count % 2 == 1:
                odd_count += 1
                odd_char = ch
            half_counts[ch] = count // 2
            
        if (n % 2 == 0 and odd_count != 0) or (n % 2 == 1 and odd_count != 1):
            return ""
        
        total_half = sum(half_counts.values()) # m
        
        def build_palindrome(half: str) -> str:
            if n % 2 == 0:
                return half + half[::-1]
            else:
                return half + odd_char + half[::-1]
        
        candidates = []
        
        # Case 1: First half exactly matches target[:m]
        target_half = target[:m]
        target_half_counts = Counter(target_half)
        if all(half_counts.get(ch, 0) == count for ch, count in target_half_counts.items()):
            full = build_palindrome(target_half)
            if full > target:
                candidates.append(full)
                
        # Case 2: Diverge at index i in the first half
        for i in range(m - 1, -1, -1):
            pref = target[:i]
            pref_counts = Counter(pref)
            
            # Check if target[:i] can be formed
            if any(half_counts.get(ch, 0) < count for ch, count in pref_counts.items()):
                continue
            
            rem_counts = {ch: half_counts[ch] - pref_counts.get(ch, 0) for ch in half_counts}
            
            # Find the smallest character greater than target[i]
            target_ch = target[i]
            valid_chars = sorted([ch for ch in rem_counts if rem_counts[ch] > 0 and ch > target_ch])
            
            if valid_chars:
                chosen = valid_chars[0]
                rem_counts[chosen] -= 1
                
                # Fill the rest greedily in ascending sorted order
                suffix = []
                for ch in sorted(rem_counts.keys()):
                    suffix.append(ch * rem_counts[ch])
                    
                first_half = pref + chosen + "".join(suffix)
                full = build_palindrome(first_half)
                candidates.append(full)
                # Since we iterate backwards from m-1 to 0, the first match at each position is optimal
                break

        if not candidates:
            return ""
            
        return min(candidates)
        