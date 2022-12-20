class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num%2 for num in nums]
        count = defaultdict(int)
        ans = 0
        count[0] = 1
        total = 0
        for i in nums:
            total+=i
            ans+=count.get(total - k,0)
            count[total]+=1
        return ans
            
            