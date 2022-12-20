class Solution:
    def totalFruit(self, f: List[int]) -> int:
        dic = defaultdict(int)
        left,right,ans = 0,0,0
        while right < len(f):  
            if len(dic) == 2 and f[right] not in dic:
                dic[f[left]]-=1
                if dic[f[left]]==0:
                    del dic[f[left]]
                left+=1
            else:
                dic[f[right]]+=1
                right+=1
            ans = max(ans,right - left)
        return ans
        
#         time -> O(2 * n) -> O(n) where n is len(f)
#         space -> O(2) -> O(1) -> constant space 
        
        