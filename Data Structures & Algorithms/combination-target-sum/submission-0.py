class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        ans = []

        def dfs(i: int, cur: List[int], s: int) -> None:
            if i >= N or s > target:
                return
            
            if s == target:
                ans.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i, cur, s + nums[i])
            cur.pop()
            dfs(i + 1, cur, s)

        dfs(0, [], 0)
        return ans