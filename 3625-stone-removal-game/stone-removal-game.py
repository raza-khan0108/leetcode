class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        turns_taken = 0

        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            turns_taken += 1

        # An odd number of successful turns means Alice took the last turn,
        # so Bob is the player who cannot move.
        return turns_taken % 2 == 1