class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        m = len(grid[0])
        seen = defaultdict(int)

        for r in range(n):
            for c in range(m):
                num = grid[r][c]
                seen[num] += 1

        for i in range(1, n*n + 1):
            if seen[i] == 2:
                repeated = i

            if seen[i] == 0:
                missing = i

        return [repeated, missing]

        

        