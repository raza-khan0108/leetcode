class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n // 2]

        return sum(abs(number - median) for number in nums)
        