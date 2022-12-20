class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left,right,ans = 0, 0,0
        dic = defaultdict(int)
        if len(s) < 3:
            return 0
        while right < 3:
            dic[s[right]]+=1
            right+=1
        while right <= len(s):
            flag = True
            for i in dic:
                if dic[i] > 1:
                    flag = False
                    break
            if flag:
                ans+=1
            dic[s[left]]-=1
            if right >= len(s):
                break
            dic[s[right]]+=1
            left+=1
            right+=1
        return ans
    
            
            
        