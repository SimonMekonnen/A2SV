# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain: 'MountainArray') -> int:
        
        
        c = mountain.length()
        left = 0
        right  = c - 1
        mything = 0
        while left <= right:
            mid = (right + left) // 2
         
            if mid == 0:
                left = mid + 1
                continue
            elif mid == c - 1:
                right = mid - 1
                continue
            l = mountain.get(mid - 1)
            now = mountain.get(mid)
            r = mountain.get(mid + 1)
            if l < now > r:
                mything = mid
                break
            if l > now:
                right = mid - 1
            else:
                left = mid + 1
                
                
        left = 0 
        right = mything
        myanswer = -1
   
        while left <= right:
            mid = (left + right)//2
            g =  mountain.get(mid)
            if g > target:
                right = mid - 1
            elif g < target:
                left = mid + 1
            else:
                return mid
        
        left = mything + 1
        right = c - 1
        myanswer = -1
        while left <= right:
            mid = (left + right)//2
            g = mountain.get(mid)
            if  g > target:
                left = mid + 1
            elif g < target:
                right = mid - 1
            else:
                return mid
        
        return -1
            