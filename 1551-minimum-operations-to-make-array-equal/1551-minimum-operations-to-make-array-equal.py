class Solution:
    def minOperations(self, n: int) -> int: 
        ans = 0
        for i in range(n // 2):
            ans += (n - (2 * i + 1))
        return ans
            