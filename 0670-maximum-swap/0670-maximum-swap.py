class Solution:
    def maximumSwap(self, num: int) -> int:
        
        nums = [i for i in str(num)]
        for i in range(len(nums)):
            m = i 
            for j in range(i,len(nums)):
                if int(nums[m]) <= int(nums[j]):
                    m = j
            
            nums[m],nums[i] = nums[i],nums[m]
            if nums[i]!=nums[m]:
                break
        return int("".join(nums))
                
                
        