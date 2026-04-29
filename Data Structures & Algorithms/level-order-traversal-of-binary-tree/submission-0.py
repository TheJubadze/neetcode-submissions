# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque()
        q.append(root)
        while len(q):
            qlen = len(q)
            curr = []
            while qlen:
                qlen -= 1
                el = q.popleft()
                curr.append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            ans.append(curr)
        return ans
