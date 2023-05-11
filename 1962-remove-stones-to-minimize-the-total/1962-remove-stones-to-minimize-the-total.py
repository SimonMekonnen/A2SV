class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= (-1)
            
        heapify(piles)
        while k and piles:
            c = heappop(piles)//2
            heappush(piles,c)
            k-=1
         
        
        return -(sum(piles))
        
        