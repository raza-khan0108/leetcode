class Solution:
    def minMoves(self, nums: list[int]) -> int:
        smallest = min(nums)

        return sum(number - smallest for number in nums)
        