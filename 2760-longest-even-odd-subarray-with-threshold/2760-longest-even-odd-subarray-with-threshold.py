class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                ans = max(1,ans)
                last = 0
                for j in range(i + 1, n):
                    if nums[j] % 2 != last and nums[j] <= threshold:
                        last = 1 - last
                        ans = max(ans, j - i + 1)
                    else:
                        break
        return ans