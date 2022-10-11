class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        dic = defaultdict(int)
        for right in range(0,len(s)):
            dic[s[right]]+=1
            while ((right - left +1) - max(dic.values())) > k:
                dic[s[left]]-=1
                left+=1
            ans = max(ans,right - left + 1)
        return ans

                
                
        