class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def helper(arr,k):
            if len(arr) == 1:
                return arr[0]
            index = random.randint(0,len(arr) - 1)
            num = arr[index]
            left = []
            right = []
            
            for i in range(0,len(arr)):
                if i == index:
                    continue
                if arr[i] > num:
                    right.append(arr[i])
                else:
                    left.append(arr[i])
        
            if len(right) >= k:
                return helper(right,k)
            elif len(right) == k - 1:
                return num
            else:
                return helper(left,k - len(right) - 1)
        
        return (helper(nums,k))
        
        
 
            
        