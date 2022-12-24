class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        ans = 0
        
        for val in c.values():
            ans += (((val/2) * (1 + val)) - val)
        
        return int(ans)

        
                    
        