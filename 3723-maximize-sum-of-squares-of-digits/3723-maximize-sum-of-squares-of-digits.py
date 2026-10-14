class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        digits = []
        while sum >= 9:
            digits.append("9")
            sum -= 9

        if sum:
            digits.append(str(sum))

        digits.extend("0" for _ in range(num - len(digits)))
        return "".join(digits)