class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        index = [i for i in range(len(intervals))]
        
        index.sort(key = lambda x : intervals[x][0])
        
        ans = []
        
        for i in intervals:
            
            left = 0
            right = len(index) - 1
            val = i[1]
            l = -1
            while left <= right:
                
                mid = (left + right)//2
                n = index[mid]
                
                if intervals[n][0] < val:
                    left = mid + 1
                
                else:
                    l = index[mid]
                    right = mid - 1
            
            ans.append(l)
            
            
            
        
        return ans
                    
        
        
        