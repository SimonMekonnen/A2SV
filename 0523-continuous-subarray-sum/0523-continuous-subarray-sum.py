class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre = defaultdict(int)
        pre[0] = 1
        total = 0
        ans = 0
        only= 0
        for i in nums:
            if i % k == 0:
                only+=1
            total+=i
            ans+=pre.get(total % k,0)
            pre[total % k] += 1
        return only!=ans
        
        