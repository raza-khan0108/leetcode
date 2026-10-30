from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, weight in edges:
            graph[u].append((v, weight))

        # State: (node, consecutive copies of labels[node])
        # Since the current node determines the last label, no separate
        # last_label field is needed.
        dist = [[float("inf")] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]  # (total_weight, node, run_length)

        while heap:
            cost, node, run_length = heapq.heappop(heap)

            if cost != dist[node][run_length]:
                continue

            if node == n - 1:
                return cost

            for nxt, weight in graph[node]:
                if labels[nxt] == labels[node]:
                    next_run = run_length + 1
                    if next_run > k:
                        continue
                else:
                    next_run = 1

                new_cost = cost + weight
                if new_cost < dist[nxt][next_run]:
                    dist[nxt][next_run] = new_cost
                    heapq.heappush(heap, (new_cost, nxt, next_run))

        return -1