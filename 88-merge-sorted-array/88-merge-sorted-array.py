class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        im = m - 1
        iN = n - 1
        to = m + n - 1
        while iN>= 0:
            if im >= 0 and nums1[im] >= nums2[iN]:
                nums1[to] = nums1[im]
                im-=1
            else:
                nums1[to] = nums2[iN]
                iN-=1
            to-=1
        
                
        
        