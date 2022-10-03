class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        ans = defaultdict(lambda: -1)
        for i in nums2:
            while stk and stk[-1] < i:
                c = stk.pop()
                ans[c] = i
            stk.append(i)
        for i in range(len(nums1)):
            nums1[i] = ans[nums1[i]]
        return nums1
            
                
        
        
     
                        
        