class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(i) for i in str(n)]
        i = j = r = len(nums)-1
        while i > 0 and nums[i]<=nums[i-1]:
            i-=1
        if i == 0:
            return -1
        else:
            while j > 0 and nums[i - 1]>= nums[j]:
                j-=1
            
            nums[j],nums[i-1] = nums[i-1],nums[j]
            l = i 
            while l < r:
                nums[r],nums[l] = nums[l],nums[r]
                l+=1
                r-=1
        nums = [str(i) for i in nums]
        ans = int("".join(nums)) 
        return ans if ans <= 2147483647 else -1
    
            
        
        