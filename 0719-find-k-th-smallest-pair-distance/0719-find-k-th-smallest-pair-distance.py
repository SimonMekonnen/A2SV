class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left = 0 
        right = max(nums)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
        
            count = 0
            l = 0
            for r in range(len(nums)):
                while nums[r] - nums[l]  > mid:
                    l += 1
                
                count += (r - l)
            
            
            if count >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
            
    