class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k: int) -> bool:
            time = 0
            for p in piles:
                time += math.ceil(p / k)
                if h < time:
                    return False
            return time <= h
        
        lo, hi = 1, max(piles)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if check(mi):
                hi = mi
            else:
                lo = mi + 1
        return hi
