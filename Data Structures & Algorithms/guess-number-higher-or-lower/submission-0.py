# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            gu = guess(mi)
            if gu > 0:
                lo = mi + 1
            elif gu < 0:
                hi = mi - 1
            else:
                return mi
        return 0