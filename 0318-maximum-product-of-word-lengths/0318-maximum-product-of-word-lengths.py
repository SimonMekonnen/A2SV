class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        b = [set(i) for i in words]
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1,len(words)):
                flag = True
                for k in b[i]:
                    
                    if k in b[j]:
                        flag = False
                if flag:
                    ans = max(len(words[i]) * len(words[j]), ans)
        return ans
                
        