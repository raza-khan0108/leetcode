from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                total = 0
                stack = [(r, c)]
                total += grid[r][c]
                grid[r][c] = 0  # Mark as visited

                while stack:
                    x, y = stack.pop()

                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < rows
                            and 0 <= ny < cols
                            and grid[nx][ny] != 0
                        ):
                            total += grid[nx][ny]
                            grid[nx][ny] = 0
                            stack.append((nx, ny))

                if total % k == 0:
                    count += 1

        return count