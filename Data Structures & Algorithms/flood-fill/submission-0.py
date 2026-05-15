class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C, Color = len(image), len(image[0]), image[sr][sc]
        visited = [[False for _ in range(C)] for _ in range(R)]
        def isValid(row, col):
            return 0 <= row < R and 0 <= col < C and not visited[row][col] and image[row][col] == Color
        def dfs(row, col):
            if not isValid(row, col):
                return
            image[row][col] = color
            visited[row][col] = True
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        dfs(sr, sc)
        return image

            