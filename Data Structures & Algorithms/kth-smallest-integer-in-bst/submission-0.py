# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        def fill(root: Optional[TreeNode]) -> None:
            nonlocal ans
            if not root or ans != -1:
                return

            nonlocal k

            fill(root.left)
            k -= 1
            if k == 0:
                ans = root.val
                return
            fill(root.right)

        fill(root)
        return ans