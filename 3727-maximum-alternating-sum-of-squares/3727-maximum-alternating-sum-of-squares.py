class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)
        positives = (len(nums) + 1) // 2
        return sum(squares[-positives:]) - sum(squares[:-positives])