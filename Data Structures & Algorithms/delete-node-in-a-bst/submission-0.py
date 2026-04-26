# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            return self.remove(root)

        return root

    def remove(self, root: TreeNode) -> Optional[TreeNode]:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        minNode = self.findMin(root.right)
        root.val = minNode.val
        root.right = self.deleteNode(root.right, root.val)

        return root

    def findMin(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root
