class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums1)
        for i in range(len(nums1)):
                j=nums2.index(nums1[i])
                for k in range(j,len(nums2)):
                    if nums2[k]>nums1[i]:
                        ans[i]=nums2[k]
                        break
                    
        return ans
                        