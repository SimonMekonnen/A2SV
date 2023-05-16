class MedianFinder:

    def __init__(self):
        self.minarr = []
        self.maxarr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        
        if self.length % 2 == 0:
            heappush(self.minarr,num)
            heappush(self.maxarr,-heappop(self.minarr))
        else:
            heappush(self.minarr,num)
            if self.minarr[0] < -self.maxarr[0]:
                frommin = heappop(self.minarr)
                frommax = -heappop(self.maxarr)
                heappush(self.maxarr,-frommin)
                heappush(self.minarr,frommax)
        
        self.length += 1
            
            

    def findMedian(self) -> float:
        if self.length % 2 == 1:
            return -self.maxarr[0]
        else:
            return (-self.maxarr[0] + self.minarr[0]) / 2
        
        
       
            
            
        
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()