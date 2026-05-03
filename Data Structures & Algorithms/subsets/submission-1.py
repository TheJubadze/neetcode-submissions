class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        
        def bt(i: int, cur: List[int]) -> None:
            if i == N:
                ans.append(cur.copy())
                return

            cur.append(nums[i])
            bt(i + 1, cur)
            cur.pop()
            bt(i + 1, cur)

        bt(0, [])
        return ans