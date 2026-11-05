class Solution:
    def findTheDistanceValue(
        self, arr1: list[int], arr2: list[int], d: int
    ) -> int:
        count = 0

        for number1 in arr1:
            far_from_all = True

            for number2 in arr2:
                if abs(number1 - number2) <= d:
                    far_from_all = False
                    break

            if far_from_all:
                count += 1

        return count