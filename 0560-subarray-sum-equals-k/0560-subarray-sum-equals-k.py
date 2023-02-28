class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        pre = {0:1}
        count = 0
        for n in nums:
            total += n
            if total - k in pre:
                count+=pre[total - k]
            pre[total] = pre.get(total, 0) +  1
        return count


            


        

     