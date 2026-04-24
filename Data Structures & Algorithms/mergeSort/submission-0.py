# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, arr1: List[Pair], arr2: List[Pair]) -> List[Pair]:
        ans, p1, p2, N1, N2 = [], 0, 0, len(arr1), len(arr2)
        while p1 < N1 and p2 < N2:
            if arr1[p1].key <= arr2[p2].key:
                ans.append(arr1[p1])
                p1 += 1
            else:
                ans.append(arr2[p2])
                p2 += 1
        
        while p1 < N1:
            ans.append(arr1[p1])
            p1 += 1

        while p2 < N2:
            ans.append(arr2[p2])
            p2 += 1

        return ans

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        N = len(pairs)
        if N <= 1:
            return pairs
        
        mid = N // 2
        return self.merge(self.mergeSort(pairs[:mid]), self.mergeSort(pairs[mid:]))