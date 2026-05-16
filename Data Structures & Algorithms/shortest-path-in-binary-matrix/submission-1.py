class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R, C, q, dirs = len(grid), len(grid[0]), deque(), [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1)]
        seen = [[False for _ in range(C)] for _ in range(R)]
        if grid[0][0] == 0:
            q.append((0, 0, 1))
        while q:
            (row, col, dist) = q.popleft()
            if row == R - 1 and col == C - 1:
                return dist
            for (dr, dc) in dirs:
                r, c = row + dr, col + dc
                if 0 <= r < R and 0 <= c < C and grid[r][c] == 0 and not seen[r][c]:
                    q.append((r, c, dist + 1))
                    seen[r][c] = True
        
        return -1