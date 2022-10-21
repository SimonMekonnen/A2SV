class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        pre = {0:-1}
        ans = 0
        for i,n in enumerate(nums):
            count-=n==0
            count+=n==1
            if count in pre:
                ans = max(ans,i - pre[count])
            else:
                pre[count] = i
        return ans
            
     
        
        
        