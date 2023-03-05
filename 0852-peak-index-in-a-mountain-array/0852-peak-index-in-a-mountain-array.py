class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left = -1 
        
        right = len(arr)
        
        while left + 1 < right:
            
            mid = (right + left)//2
            if mid == 0:
                left = mid
            elif mid == len(arr) - 1:
                right = mid
            elif arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                
                return mid
            
            elif arr[mid] < arr[mid - 1]:
                
                right = mid
            
            else:
                
                left = mid
                
        

                