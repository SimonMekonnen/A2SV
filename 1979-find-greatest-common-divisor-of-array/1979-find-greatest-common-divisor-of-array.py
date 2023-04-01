class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def helper(a,b):
            if b == 0:
                return a
            return helper(b,a % b)
        
        return helper(max(nums),min(nums))
        