class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])
        visited = set()
        ogcolor = image[sr][sc]
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return None

            if image[r][c] != ogcolor:
                return None
            
            if ((r, c)) in visited:
                return None

            if image[r][c] == ogcolor:
                image[r][c] = color
                visited.add((r, c))


            for dr, dc in directions:
                newRow = r + dr
                newCol = c + dc
                dfs(newRow, newCol)


        
        dfs(sr, sc)

        return image


        