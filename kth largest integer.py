class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums.sort(key= lambda x:int(x), reverse=True)
        return nums[k-1]