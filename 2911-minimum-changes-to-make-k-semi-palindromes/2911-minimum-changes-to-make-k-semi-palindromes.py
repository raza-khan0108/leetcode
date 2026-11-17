from math import inf

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # cost[left][right] = minimum changes to make s[left:right + 1]
        # a semi-palindrome.
        cost = [[inf] * n for _ in range(n)]

        for left in range(n):
            for right in range(left + 1, n):  # length must be at least 2
                length = right - left + 1
                best = inf

                # d must divide the substring length, and d < length.
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Check each group of characters that are d positions apart.
                    for offset in range(d):
                        group_length = (length - 1 - offset) // d + 1

                        for pair in range(group_length // 2):
                            first = left + offset + pair * d
                            second = left + offset + (group_length - 1 - pair) * d

                            if s[first] != s[second]:
                                changes += 1

                    best = min(best, changes)

                cost[left][right] = best

        # previous[end] = best cost to split the first `end` chars
        # into the number of parts from the previous DP round.
        previous = [inf] * (n + 1)
        previous[0] = 0

        for parts in range(1, k + 1):
            current = [inf] * (n + 1)

            # `end` is the exclusive end index of the current partition.
            for end in range(parts * 2, n + 1):
                # The last substring is s[start:end], with length >= 2.
                for start in range((parts - 1) * 2, end - 1):
                    if previous[start] != inf:
                        current[end] = min(
                            current[end],
                            previous[start] + cost[start][end - 1]
                        )

            previous = current

        return previous[n]