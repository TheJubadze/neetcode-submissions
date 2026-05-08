class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, -n)
        while k > 1:
            k -= 1
            heapq.heappop(h)
        
        return -heapq.heappop(h)