class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[1,0]]
        
        for i in range(1,len(nums1)):
            #notswap can join with it prev index
            #swaped dp
            first = nums2[i - 1]
            second = nums1[i - 1]
            
            curfirst = nums1[i]
            cursecond = nums2[i]
            candidate  = inf
            if curfirst > first and cursecond > second:
                candidate = min(candidate,dp[i-1][0])
            
            first = nums1[i - 1]
            second = nums2[i - 1]
            
            if curfirst > first and cursecond > second:
                candidate = min(candidate,dp[i-1][1])
            
            
            notswap = candidate
            
            
            #swapping current
            
            first = nums2[i - 1]
            second = nums1[i - 1]
            
            curfirst = nums2[i]
            cursecond = nums1[i]
            candidate  = inf
            if curfirst > first and cursecond > second:
                candidate = min(candidate,dp[i-1][0] + 1)
            
            first = nums1[i - 1]
            second = nums2[i - 1]
            
            if curfirst > first and cursecond > second:
                candidate = min(candidate,dp[i-1][1] + 1)
            
            swap = candidate
            
            dp.append([swap,notswap])

        return min(dp[-1])
            
            
                