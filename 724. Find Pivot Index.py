class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        x = -1
        pre = [0]
        total = 0
        for num in nums:
            total += num
            pre.append(total)
        for i in range(1,len(pre)):
            if pre[i-1] == pre[-1] - pre[i]:
                return i - 1
        return -1
        
            