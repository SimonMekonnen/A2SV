class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set()
        
        for i in nums:
            ans.add(i)
            ans.add(int(str(i)[::-1]))
            
        return len(ans)
            
        