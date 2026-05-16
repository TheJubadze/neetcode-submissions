class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C, q, fresh, ans = len(grid), len(grid[0]), deque(), 0, -1
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if not fresh:
            return 0
        
        while q:
            qlen = len(q)
            for _ in range(qlen):
                (row, col) = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r, c = row + dr, col + dc
                    if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            ans += 1
        
        return (ans or -1) if not fresh else -1