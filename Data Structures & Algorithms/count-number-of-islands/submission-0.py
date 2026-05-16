class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(row, col):
            if not (0 <= row < R and 0 <= col < C and grid[row][col] != "0"):
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)

        return ans
