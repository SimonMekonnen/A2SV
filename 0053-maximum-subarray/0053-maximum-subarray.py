class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        Curr = 0
        for i in nums:
            Curr = max(Curr,0)
            Curr+=i
            _max = max(_max,Curr)
        return _max
       
                
            
        