class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        save, read1, read2 = len(nums1) - 1, m - 1, n - 1
        while read1 >= 0 and read2 >= 0:
            if nums1[read1] < nums2[read2]:
                nums1[save] = nums2[read2]
                read2 -= 1
            else:
                nums1[save] = nums1[read1]
                read1 -= 1
            save -= 1
        
        while read2 >= 0:
            nums1[save] = nums2[read2]
            read2 -= 1
            save -= 1
