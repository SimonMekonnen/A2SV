class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        pre = defaultdict(lambda : 0)
        pre[0] =  1
        for num in nums:
            total +=num
            if total - k in pre:
                count+=pre[total - k]
            pre[total]+=1
        return count
    
        