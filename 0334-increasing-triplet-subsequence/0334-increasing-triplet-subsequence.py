class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        arr1 = [nums[0]]
        arr2 =  [nums[-1]]
        for i in range(1,len(nums)):
            arr1.append(min(arr1[-1],nums[i]))
            arr2.append(max(arr2[-1] ,nums[len(nums) - 1 - i]))
        for i in range(len(nums)):
            if arr1[i] < nums[i] < arr2[len(nums) - 1 - i]:
                return True
        return False
        
        

        