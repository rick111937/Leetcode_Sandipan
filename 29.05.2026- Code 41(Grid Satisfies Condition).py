from typing import List
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        for c in range(cols):
            for r in range(1, rows):
                if grid[r][c] != grid[r - 1][c]:
                    return False
        for r in range(rows):
            for c in range(1, cols):
                if grid[r][c] == grid[r][c - 1]:
                    return False
        return True