class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(-s)
        heapq.heapify(heap)
        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            if a < b:
                heapq.heappush(heap, -(b - a))
            elif a > b:
                heapq.heappush(heap, -(a - b))
        
        return 0 if not len(heap) else -heap[0]