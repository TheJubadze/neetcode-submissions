class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(row, col):
            if not (0 <= row < R and 0 <= col < C and grid[row][col] == 1):
                return 0
            
            grid[row][col] = 0
            area = 1
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)
            
            return area

        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        
        return ans