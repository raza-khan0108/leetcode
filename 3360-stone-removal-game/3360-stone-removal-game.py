class Solution:
    def canAliceWin(self, n: int) -> bool:
        to_remove = 10
        turns = 0

        while n >= to_remove:
            n = n - to_remove
            to_remove = to_remove - 1
            turns = turns + 1


        return turns % 2 == 1