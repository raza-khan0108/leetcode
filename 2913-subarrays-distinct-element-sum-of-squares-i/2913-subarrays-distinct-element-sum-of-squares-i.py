class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0

        for start in range(len(nums)):
            seen = set()

            for end in range(start, len(nums)):
                seen.add(nums[end])
                distinct_count = len(seen)
                total += distinct_count * distinct_count

        return total
        