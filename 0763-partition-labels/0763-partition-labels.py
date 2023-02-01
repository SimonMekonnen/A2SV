class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
        ans = []  
        left = 0
        right = dic[s[0]]
        i = 0
        while i < len(s):
            
            right = max(dic[s[i]],right)
            if i == right:
         
                ans.append(right - left + 1)
                left = right + 1
                
    
            i+=1
            
        return ans
                
        
#         count  = Counter(s)
#         new = defaultdict(int)
#         ans = []
        
#         for i in s:
#             new[i]+=1
#             Flag = True
#             for j in new:
#                 if new[j] != count[j]:
#                     Flag = False
#             if Flag:
#                 ans.append(sum(new.values()))
#                 new.clear()

#         return ans
        
        
        