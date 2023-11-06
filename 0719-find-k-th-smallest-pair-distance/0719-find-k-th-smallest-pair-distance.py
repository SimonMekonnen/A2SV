class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left = 0 
        right = 10**6
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            count = 0
            
            for i in range(len(nums) - 1):
                cur_index = bisect_right(nums,mid + nums[i])
                
                c = cur_index
                if c >= len(nums) or nums[c] > mid + nums[i]:
                    c -= 1
                
                count += (c - i)
            
            if count >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
            
    