class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C, Color = len(image), len(image[0]), image[sr][sc]
        if color == Color:
            return image
        def isValid(row, col):
            return 0 <= row < R and 0 <= col < C and image[row][col] == Color
        def dfs(row, col):
            if not isValid(row, col):
                return
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        dfs(sr, sc)
        return image

            