class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_s = ""

            for start in range(0, len(s), k):
                group = s[start:start + k]
                digit_total = sum(int(digit) for digit in group)
                next_s += str(digit_total)

            s = next_s

        return s