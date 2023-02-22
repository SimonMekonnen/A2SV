class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], f: int, s: int) -> int:
        
        why  = []
        second = []
        total = 0
        for right in range(f):
            total += nums[right]
            
        left = 0
        
        why.append((left,right,total))
        for right in range(f,len(nums)):
            
            total += nums[right]
            total -= nums[left]
            
          
            left += 1
            why.append((left,right,total))
            
        total = 0
        for right in range(s):
            total += nums[right]
            
        left = 0
        
        second.append((left,right,total))
        for right in range(s,len(nums)):
            
            total += nums[right]
            total -= nums[left]
            
          
            left += 1
            second.append((left,right,total))
        ans = 0
        for i in why:
            
            for j in second:
                
                if j[0] <= i[0] <=  j[1] or j[0] <= i[1] <=  j[1] or i[0] <= j[0] <=  i[1] or i[0] <= j[1] <=  i[1]:
                    pass
                else:
                    ans = max(ans,i[2] + j[2])
            
        
        
        return ans
                
        
        

            
            
        
        
        
        
        