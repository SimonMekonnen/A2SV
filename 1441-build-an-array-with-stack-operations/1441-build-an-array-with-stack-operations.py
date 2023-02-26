class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 1
        j = 0
        while i <= target[-1]:
            ans.append("Push")
            if i == target[j]:
                j+=1
            else:
                ans.append("Pop")
            i += 1
        return ans
        
        
        