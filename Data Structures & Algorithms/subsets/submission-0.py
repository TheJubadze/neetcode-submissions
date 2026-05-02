class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        def bt(i: int, cur: List[int]) -> None:
            ans.append(cur[::])
            for j in range(i, N):
                cur.append(nums[j])
                bt(j + 1, cur)
                cur.pop()

        bt(0, [])
        return ans