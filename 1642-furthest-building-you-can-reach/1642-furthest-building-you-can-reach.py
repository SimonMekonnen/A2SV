class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        
        heap = []
        count  = 0
        for i in range(len(h) - 1):
            togo = h[i + 1] - h[i]
            if togo > 0:
                heappush(heap,togo)
                if len(heap) > l:
                    b -= heappop(heap)
                    if b < 0:
                        return count
            count += 1
        return count
                    
                
        