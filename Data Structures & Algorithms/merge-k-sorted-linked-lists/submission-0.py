# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        N = len(lists)

        indices = []
        for i in range(N):
            if lists[i]:
                indices.append(lists[i])

        heapq.heapify(indices)

        ans = ListNode()
        ptr = ans

        while len(indices):
            cur = heapq.heappop(indices)
            ptr.next = cur
            ptr = cur
            if cur and cur.next:
                heapq.heappush(indices, cur.next)

        return ans.next
