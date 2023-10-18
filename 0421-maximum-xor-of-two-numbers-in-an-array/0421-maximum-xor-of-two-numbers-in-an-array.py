class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        
        ans = ""
        n = len(bin(max(nums))) - 2
        
        for i in range(n - 1 ,-1,-1):
            
            dic = set()
            for j in nums:
                dic.add(j >> i)
            cur = int(ans + "1",2)
            pos = 0
            for i in dic:
                if cur ^ i in dic:
                    pos = 1
            if pos:
                ans = bin(cur)[2: ]
            else:
                ans += "0"
        return int(ans,2)
            
                