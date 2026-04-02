class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            # 1. Success Base Case
            if i == len(word):
                return True
            
            # 2. Failure Base Cases (Out of bounds, wrong char, or already visited)
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[i] or (r, c) in visited):
                return False
            
            # 3. Mark the path
            visited.add((r, c))
            
            # 4. Explore neighbors (i + 1)
            # This is a cleaner way than a manual for-loop with directions
            res = (dfs(r+1, c, i+1) or 
                   dfs(r-1, c, i+1) or 
                   dfs(r, c+1, i+1) or 
                   dfs(r, c-1, i+1))
            
            # 5. Backtrack: Clean up the state
            visited.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                # Start DFS if the first letter matches
                if board[r][c]==word[0]:
                    if dfs(r, c, 0):
                        return True
        return False