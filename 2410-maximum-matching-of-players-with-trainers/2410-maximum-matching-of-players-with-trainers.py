class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        
        p.sort()
        t.sort()
        
        left = 0
        right = 0
        ans = 0
        
        while left < len(p) and right < len(t):
            
            if p[left] <= t[right]:
                right+=1
                left+=1
                ans+=1
            
            else:
                right += 1
        
        return ans