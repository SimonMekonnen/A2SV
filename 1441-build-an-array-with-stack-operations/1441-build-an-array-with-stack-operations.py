class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        now = [i for i in range(1,n+1)]
        ans = []
        
        while now[-1] != target[-1]:
            now.pop()
        i = 0
        j = 0
        while i < len(now):
            
            if now[i] == target[j]:
                j+=1
                i+=1
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
                i += 1
        
          
            
        return ans
        
        
        