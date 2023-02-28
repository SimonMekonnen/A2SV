class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        oddCount = ans = left = 0
        for right in range(n):
            oddCount += nums[right] % 2
            
            while oddCount >= k :
                oddCount -= nums[left] % 2
                left += 1
                
            ans += right - left + 1
            
        n = len(nums)
        oddCount = ano = left = 0
        
        for right in range(n):
            oddCount += nums[right] % 2
            
            while oddCount > k :
                oddCount -= nums[left] % 2
                left += 1
                
            ano += right - left + 1
            
        return ano - ans
            


    