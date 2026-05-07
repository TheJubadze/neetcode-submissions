class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for [x, y] in points:
            heapq.heappush(h, (math.sqrt(x ** 2 + y ** 2), [x, y]))

        ans = []
        while k:
            ans.append(heapq.heappop(h)[1])
            k -= 1

        return ans