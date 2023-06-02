class Solution:
    def numDecodings(self, s: str) -> int:
        possible = set([str(i) for i in range(1,27)])
        @cache
        def dp(index,prev):
            if prev not in possible:
                return 0
            if index >= len(s):
                return 1
            add = dp(index + 1,s[index])
            notadd = 0
            if index < len(s) - 1:
                notadd = dp(index + 2,s[index : index + 2])
            return add + notadd
        return dp(0,s[0])
            
            
            
            