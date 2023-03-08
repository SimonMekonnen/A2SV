class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left = 1
        right = max(nums)
        
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for i in nums:
                total += ceil(i / mid)
                
            if total > threshold:
                
                left = mid + 1
            
            else:
                right = mid - 1
        
        return left
        