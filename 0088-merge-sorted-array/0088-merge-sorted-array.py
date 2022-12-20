class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m
        r = n 
        k =  m + n
        nums1.insert(0,-math.inf)
        nums2.insert(0,-math.inf)
        while k >= 0:
            if nums1[l] > nums2[r]:
                nums1[k] = nums1[l]
                l-=1
            else:
                nums1[k] = nums2[r]
                r-=1
            k-=1
        nums1.pop(0)
            
                
     
        
                
        
        