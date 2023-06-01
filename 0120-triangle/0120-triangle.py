class Solution:
    def minimumTotal(self, tr: List[List[int]]) -> int:  
        @cache
        def dp(row,col):
            if row >= len(tr):
                return 0
            return tr[row][col] + min(dp(row + 1,col),dp(row + 1,col + 1))
    
        return dp(0,0)
        