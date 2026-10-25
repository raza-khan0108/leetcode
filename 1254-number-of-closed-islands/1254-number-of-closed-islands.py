class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def sink(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return

            grid[r][c] = 1  # Mark this land cell as visited
            sink(r + 1, c)
            sink(r - 1, c)
            sink(r, c + 1)
            sink(r, c - 1)

        # Remove every island that touches the boundary; it cannot be closed.
        for r in range(rows):
            sink(r, 0)
            sink(r, cols - 1)
        for c in range(cols):
            sink(0, c)
            sink(rows - 1, c)

        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    sink(r, c)

        return closed_islands