class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, i):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            
            if board[row][col] != word[i]:
                return False

            if (row, col) in visited:
                return False
            
            if i == len(word) - 1:
                return True

            visited.add((row, col))

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                if dfs(new_row, new_col, i + 1):
                    return True
                

            visited.remove((row,col))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False



        