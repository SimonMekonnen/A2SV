class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        def good(arr):
            
            for i in arr:
                if i >= 2:
                    return False
            return True
        
        bits = [0] *  32
        
        left = 0
        ans = 1
        for right in range(len(nums)):
            bit = list(bin(nums[right])[2:])
            bit.reverse()
            for i in range(len(bit)):
                bits[i] += int(bit[i])
            
            while not good(bits):
                bit = list(bin(nums[left])[2:])
                bit.reverse()
                for i in range(len(bit)):
                    bits[i] -= int(bit[i])
                left += 1
            ans = max(right  - left + 1,ans)
        return ans
                
        
        
        
        