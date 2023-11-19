class Solution:
    def minimumSteps(self, s: str) -> int:
        
        
        ans = [0]
        count = 0
        for i in s:
            if i == '1':
                ans.append(ans[-1] + 1)
            else:
                count += ans[-1]
                ans.append(ans[-1])
               
        return count
        