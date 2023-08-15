class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        for i in range(len(strs)):
            count = Counter(strs[i])
            strs[i] = [count["0"],count["1"]]
        @cache
        def dp(index,one,zero):
            if index >= len(strs):
                return 0
            if one > n or zero > m:
                return 0
            take = 0
            if one + strs[index][1] <= n and zero + strs[index][0] <= m:
                take = 1 + dp(index + 1,one + strs[index][1],zero + strs[index][0])
            notake = dp(index + 1,one,zero)
            return max(take,notake)
        return dp(0,0,0)
        
        
            