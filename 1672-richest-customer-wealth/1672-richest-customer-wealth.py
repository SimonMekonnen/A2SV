class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        b = [ sum(i) for i in accounts]
        return max(b)
        