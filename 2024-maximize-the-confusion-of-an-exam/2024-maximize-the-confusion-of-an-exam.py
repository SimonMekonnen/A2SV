class Solution:
    def maxConsecutiveAnswers(self, answer: str, k: int) -> int:
        l= 0
        T  = 0
        F = 0
        ans = 0
        for r in range(0,len(answer)):
            T+=answer[r]=="T"
            F+=answer[r]=="F"
            while r - l + 1 - max(T,F) > k:
                 T-=answer[l]=="T"
                 F-=answer[l]=="F"
                 l+=1
            ans = max(ans,r - l + 1)
        return ans
                 
                
        
     
            
                
        