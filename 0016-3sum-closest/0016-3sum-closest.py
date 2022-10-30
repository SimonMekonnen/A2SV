class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = math.inf
        for i in range(0,len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                _sum = nums[l] + nums[r] + nums[i]
                if abs(target - _sum) < abs(target - ans):
                    ans = _sum   
                if _sum > target:
                    r-=1
                elif _sum < target:
                    l+=1
                else:
                    return ans
        return ans
                
                
            
        