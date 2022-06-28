class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        indicies = []
        for i in range(len(nums)):
            if target == nums[i]:
                indicies.append(i)
        return indicies
                