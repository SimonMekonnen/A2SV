class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        nums = [[position[i],speed[i]] for i in range(len(speed))]
        
        nums.sort()
        
        stk  = []
        
        for i in nums:
            while stk and (target - i[0]) / i[1] >= stk[-1]:
                stk.pop()
            
            stk.append((target - i[0]) / i[1])
        
        return len(stk)