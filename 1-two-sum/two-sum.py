class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, number in enumerate(nums):
            needed = target - number

            if needed in seen:
                return [seen[needed],i]
            
            seen[number] = i
        
        return []