class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited=set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        count=0
        maxArea =0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in visited or grid[i][j]==0:
                    continue
                if grid[i][j]==1:
                    area=1
                    q= deque([(i,j)])
                    visited.add((i,j))
                    while q:
                        for k in range(len(q)):
                            r,c= q.popleft()
                            for dr, dc in directions:
                                row = r +dr
                                col = c +dc
                                if 0 <= row < ROWS and 0 <= col < COLS and (row,col) not in visited and grid[row][col] == 1:
                                    q.append((row,col))
                                    visited.add((row,col))
                                    area+=1
                    maxArea= max(maxArea, area)
        return maxArea
                
