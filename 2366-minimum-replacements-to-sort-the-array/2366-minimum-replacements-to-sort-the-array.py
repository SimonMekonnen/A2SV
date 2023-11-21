class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0 
        sofarmin = nums[-1]
        for i in range(n - 2,-1,-1):
            left = 1
            right = nums[i]
            can = -1
            while left <= right:
                mid = (right + left) // 2

                cur = math.ceil(nums[i] / mid)

                if cur > sofarmin:
                    left = mid + 1
                else:
                    can = mid
                    right = mid - 1

            ans += (can - 1)
            sofarmin = nums[i] // can
        
        return ans

