class Solution:
    def minimumCost(
        self,
        cost1: int,
        cost2: int,
        costBoth: int,
        need1: int,
        need2: int
    ) -> int:
        # Use type 3 items for the amount both requirements share.
        shared = min(need1, need2)
        cost = shared * min(costBoth, cost1 + cost2)

        # Buy single-type items for the remaining requirement.
        cost += (need1 - shared) * min(cost1, costBoth)
        cost += (need2 - shared) * min(cost2, costBoth)

        return cost