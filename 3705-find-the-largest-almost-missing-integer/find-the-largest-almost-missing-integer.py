from typing import List
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Dictionary to count how many subarrays of size k each number appears in
        subarray_counts = {}
        
        # Iterate over all possible starting indices for subarrays of size k
        for i in range(n - k + 1):
            # Extract the subarray
            subarray = nums[i : i + k]
            # Use a set to get unique elements in the current subarray
            unique_in_subarray = set(subarray)
            
            # Increment the count for each unique element
            for num in unique_in_subarray:
                subarray_counts[num] = subarray_counts.get(num, 0) + 1
                
        # Find the maximum integer that appears in exactly one subarray
        ans = -1
        for num, count in subarray_counts.items():
            if count == 1:
                ans = max(ans, num)
                
        return ans