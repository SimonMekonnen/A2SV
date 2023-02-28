class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        pre = defaultdict(lambda : 0)
        pre[0] = 1
        ans = 0
        for num in nums:
            total+=num
            ans+=(pre.get(total % k,0)) 
            pre[total % k]+=1
        return ans
            
            
        