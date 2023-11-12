class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        
        if n + n - 1 < target:
            return n * (n + 1) // 2
        left = target - 1
        removed = (left // 2)
        n += removed
        rightsum = (n  * (n + 1) // 2 ) - ((target - 1) * (target) // 2)
        
        l = (left - removed)
        
        leftsum = (l * (l + 1) // 2)
        
        return (rightsum + leftsum) % (10 ** 9 + 7)
        
      
    