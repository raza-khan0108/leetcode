class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        answer = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            previous_last = None
            sortable = True

            for start in range(0, n, k):
                block = nums[start:start + k]

                drops = [
                    i for i in range(k)
                    if block[i] > block[(i + 1) % k]
                ]

                if len(drops) > 1:
                    sortable = False
                    break

                if drops:
                    drop = drops[0]
                    cut = (drop + 1) % k
                    first = block[cut]
                    last = block[drop]
                else:
                    first = block[0]
                    last = block[-1]

                if previous_last is not None and previous_last > first:
                    sortable = False
                    break

                previous_last = last

            if sortable:
                answer += k

        return answer