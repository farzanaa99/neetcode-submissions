class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        area = 0

        def dfs(r, c):

            if r < 0 or r >= n or c < 0 or c >= m:
                return 0

            if grid[r][c] == 0 or grid[r][c] == 2:
                return 0

            grid[r][c] = 2
            area = 1

            for dr, dc in directions:
                newRow = dr + r
                newCol = dc + c
                area += dfs(newRow, newCol)

            return area

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))

        return area


        

            
            
            
        