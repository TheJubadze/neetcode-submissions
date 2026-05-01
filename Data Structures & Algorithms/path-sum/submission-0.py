# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = False
        def dfs(root: Optional[TreeNode], curSum: int) -> None:
            nonlocal ans
            if ans or not root:
                return

            if not root.left and not root.right:
                if curSum + root.val == targetSum:
                    ans = True
                return

            dfs(root.left, curSum + root.val)
            dfs(root.right, curSum + root.val)
        
        dfs(root, 0)

        return ans