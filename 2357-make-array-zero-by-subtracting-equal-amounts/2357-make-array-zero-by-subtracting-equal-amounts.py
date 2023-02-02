class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        a = set(nums)
        
        return len(a) if 0 not in a else len(a) - 1
        