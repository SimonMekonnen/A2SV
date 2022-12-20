class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        P = Counter(p)
        dic = defaultdict(int)
        n = len(p)
        right = 0
        if n > len(s):
            return []
        while right < n:
                dic[s[right]]+=1
                right+=1
        left = 0
        ans = []
        while right <= len(s):
            flag = True
            for i in P:
                if dic[i] != P[i]:
                    flag = False
            if flag == True:
                ans.append(left)
            if right == len(s):
                break
            dic[s[right]]+=1
            dic[s[left]]-=1
            left+=1
            right+=1
        return ans
    #     time -> O(26 * n) -> O(n) where n is len(s)
#         space -> O(26) -> O(1) -> constant space 
                
            
            
        