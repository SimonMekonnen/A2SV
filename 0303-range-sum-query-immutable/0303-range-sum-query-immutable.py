class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = []
        total = 0
        for num in nums:
            total+=num
            self.pre.append(total)
    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right] - self.pre[left - 1] if left != 0 else self.pre[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)