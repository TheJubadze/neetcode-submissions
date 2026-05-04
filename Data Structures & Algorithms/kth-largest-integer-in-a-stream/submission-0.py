class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = []
        for n in nums:
            self.q.append(-n)
        self.k = k
        heapq.heapify(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, -val)
        i = 0
        tmp = []
        while i < self.k:
            tmp.append(heapq.heappop(self.q))
            i += 1
        for i in range(len(tmp)):
            heapq.heappush(self.q, tmp[i])
        return -tmp[-1]
