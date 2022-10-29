class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1]*len(nums)
        if len(nums)/2 <= k:
            return ans
        b = k
        left = 0
        total = 0
        for right in range(len(nums)):
            if right - left + 1 <= (k *2 +1):
                total+=nums[right]
            else:
                ans[b]=(total//(k*2+1))
                b+=1
                total-=nums[left]
                total+=nums[right]
                left+=1
        ans[b] = (total//(k*2+1))
        return ans
        