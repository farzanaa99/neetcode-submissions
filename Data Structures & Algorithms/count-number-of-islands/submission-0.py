class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        numberOfIslands = 0
        
        def dfs(r, c):

            if r < 0 or r >= n or c < 0 or c >= m:
                return 0

            if grid[r][c] == "0":
                return 0
            
            #visited
            grid[r][c] = "0"
            
            for dr, dc in directions:
                dfs(dr+r, dc+c)


        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    numberOfIslands += 1
                    dfs(r, c)

        return numberOfIslands

        
        