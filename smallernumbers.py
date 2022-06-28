class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = [0] *(max(nums)+1)
        final = []
        for i in nums:
            count[i]+=1
        for i in nums:
            j=i-1
            k=0
            while j>=0:
                k+=count[j] 
                j-=1
            final.append(k)
        return final