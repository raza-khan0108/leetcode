from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        # Try matching prefix of length `i` where target[0...i-1] matches exactly
        for i in range(n - 1, -1, -1):
            # Check if target[0...i-1] can be formed
            prefix_counts = Counter(target[:i])
            if any(prefix_counts[ch] > total_counts[ch] for ch in prefix_counts):
                continue
            
            # Remaining characters available after matching target[:i]
            rem_counts = total_counts - prefix_counts
            
            # Find the smallest character strictly greater than target[i]
            target_char = target[i]
            candidates = sorted([ch for ch in rem_counts if ch > target_char])
            
            if candidates:
                chosen = candidates[0]
                rem_counts[chosen] -= 1
                
                # Construct remainder in ascending sorted order
                suffix = []
                for ch in sorted(rem_counts.keys()):
                    suffix.append(ch * rem_counts[ch])
                    
                return target[:i] + chosen + "".join(suffix)
                
        return ""