class Solution:
    def totalFruit(self, f: List[int]) -> int:
        dic = defaultdict(int)
        ans = 0
        left = 0
        for right in range(len(f)):
            dic[f[right]]+=1
            while len(dic) > 2:
                dic[f[left]]-=1
                if dic[f[left]] == 0:
                    del dic[f[left]]
                left+=1
            ans = max(ans,right - left + 1)  
        return ans
            

#         time -> O(2 * n) -> O(n) where n is len(f)
#         space -> O(2) -> O(1) -> constant space 
        
        