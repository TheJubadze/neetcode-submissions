class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix[0])

        def search(nums: List[int]):
            nonlocal target
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return True
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False

        s, e = 0, len(matrix) - 1
        while s <= e:
            m = s + (e - s) // 2
            if matrix[m][0] <= target <= matrix[m][N - 1]:
                return search(matrix[m])

            if target < matrix[m][0]:
                e = m - 1
            else:
                s = m + 1

        return False