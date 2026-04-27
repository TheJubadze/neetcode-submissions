# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ldep = self.getDep(root.left)
        rdep = self.getDep(root.right)
        return abs(ldep - rdep) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDep(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ldep = self.getDep(root.left)
        rdep = self.getDep(root.right)
        return max(ldep, rdep) + 1