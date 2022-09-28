class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for i in range(1,len(nums)):
            left.append(left[-1]*nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            right.append(right[-1]*nums[i+1])
        for i in range(len(nums)):
            left[i]*=right[len(nums)-1-i]
        return left
            
    
        
        
        