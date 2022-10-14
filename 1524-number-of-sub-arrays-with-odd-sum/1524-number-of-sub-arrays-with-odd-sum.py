class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_even = {0:1,1:0}
        ans = 0
        total = 0
        for i in arr:
            total+=i
            if total % 2 == 0:
                ans+=odd_even[1]
            else:
                ans+=odd_even[0]
            odd_even[total % 2]+=1
        return ans%1000000007
            
            
        
        
        
        
        
        