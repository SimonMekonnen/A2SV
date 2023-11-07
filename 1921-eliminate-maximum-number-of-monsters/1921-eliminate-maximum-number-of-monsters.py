class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        arr  = []
        for i in range(len(dist)):
            arr.append(dist[i] / speed[i])
        
        arr.sort()
        m = 0
        i = 0
        count = 0
        while i < len(dist):
            
            if m < arr[i]:
                count += 1
            else:
                break
    
            m += 1
            i += 1
        
        return count
                