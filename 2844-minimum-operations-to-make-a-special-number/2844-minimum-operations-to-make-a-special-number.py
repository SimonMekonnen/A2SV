class Solution:
    def minimumOperations(self, num: str) -> int:
        
        @cache
        def dp(index,mynum):
            if index >= len(num):     
                if mynum == 0:
                    return 0
                else:
                    return -inf  
            newmd = (mynum * 10 + int(num[index]) ) % 25
            pick = 1 + dp(index + 1,newmd)
            dontpick = dp(index + 1,mynum)
            return max(pick,dontpick)
        return len(num) - dp(0,0)