class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        right,left,totalsum,ans= 0,0,0,0
        for i in range(k):
            totalsum+=arr[right]
            right+=1
        while right<=len(arr):
            if totalsum/k>=threshold:
                ans+=1
            if right ==  len(arr):
                break
            totalsum+=arr[right]
            totalsum-=arr[left]
            left+=1
            right+=1
        return ans
    
#time complexity O(n)
#space complexity O(n)
                
        
        