class Solution:
    def maxSatisfied(self, cus: List[int], g: List[int], m: int) -> int:
        ans = 0
        sat = 0
        total = 0
        left , right = 0 , 0
        for right in range(m):
            if g[right]==1:
                ans+=cus[right]
            else:
                sat+=cus[right]
            total = max(ans,total)
        right+=1
        while right < len(cus):
            if g[right] == 1:
                ans+=cus[right]
            else:
                sat+=cus[right]
            if g[left] == 1:
                ans-=cus[left]
            total = max(ans,total)
            right+=1
            left+=1
        return total + sat
        
            
            
        