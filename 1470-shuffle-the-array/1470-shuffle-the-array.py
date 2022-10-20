class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        left = 0
        right = n
        while left < n:
            ans.append(nums[left])
            ans.append(nums[right])
            left+=1
            right+=1
        return ans
            
            
        