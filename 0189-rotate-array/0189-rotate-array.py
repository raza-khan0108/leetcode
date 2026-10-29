class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp = []
        temp = [0] * n

        if n == 0:
            return

        for i in range(n):
            temp[ (i+k) % n ] = nums[i]

        nums[:] = temp


        