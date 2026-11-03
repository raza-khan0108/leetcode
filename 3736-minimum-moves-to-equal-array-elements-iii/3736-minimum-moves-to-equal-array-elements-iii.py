class Solution:
    def minMoves(self, nums: List[int]) -> int:
        largest = max(nums)

        return sum(largest - number for number in nums)
        