class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0

            visited.add((r, c))
            perimeter = 0
            for dr, dc in directions:
                newRow = r + dr
                newCol = c + dc
                perimeter += dfs(newRow, newCol)

            return perimeter


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)





        