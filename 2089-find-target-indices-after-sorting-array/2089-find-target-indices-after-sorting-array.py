class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        solution = []

        for i,value in enumerate(nums):
            if value == target:
                solution.append(i)
        
        return solution
        
            
        