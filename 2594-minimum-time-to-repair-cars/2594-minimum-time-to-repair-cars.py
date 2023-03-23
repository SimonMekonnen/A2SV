class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        left = 1
        right = min(ranks) * cars * cars
        
        while left <= right:
            mid = (left + right)//2
            now = 0
     
            for i in ranks:
                 now += floor((((mid // i )) ** 0.5))
            
            if now < cars:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
                    
        