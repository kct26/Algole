class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        def dfs (i,j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs (i + 1, j)
            dfs (i - 1, j)
            dfs (i, j + 1)
            dfs (i, j - 1)

        for i in range (m):
            for j in range (n):
                if grid[i][j] == "1":
                    dfs (i,j)
                    cnt += 1    
        return cnt
            
