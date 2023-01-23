class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [i for i in range(len(nums))]
        ans = [i for i in range(len(nums))]
        arr.sort(key = lambda x:nums[x])
        for i in range(len(arr)):
            
            if i == 0 or nums[arr[i]] != nums[arr[i - 1]]:
                ans[arr[i]] = i
            else:
                ans[arr[i]] = ans[arr[i - 1]]
            
        return ans
        
        
        
        
            
  
         