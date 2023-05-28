class Solution:
    def divisorGame(self, n: int) -> bool:
        first = 0
        second = 1
        if n == 1:
            return 0
        for i in range(2,n + 1):
            if i % 2 == 1:
                c = second
                first = second
                second = 1 - c    
            else:
                if first * second == 0:
                    first = second
                    second = 1
                else:
                    first = second
                    second = 0 
        return second
        