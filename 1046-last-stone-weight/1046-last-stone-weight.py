class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if y - x > 0:
                heappush(stones,-(y - x))
    
        return -stones[0] if stones else 0
            
            
        