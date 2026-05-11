class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        big = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            if big < arr[i]:
                newBig = arr[i]
                arr[i] = big
                big = newBig
            else:
                arr[i] = big
        return arr