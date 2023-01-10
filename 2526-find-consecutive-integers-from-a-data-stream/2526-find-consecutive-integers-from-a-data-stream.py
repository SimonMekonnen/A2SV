class DataStream:

    def __init__(self, value: int, k: int):
        self.arr = []
        self.value = value
        self.k = k
        self.dic = defaultdict(int)
        self.count = 0
        self.left = 0

    def consec(self, num: int) -> bool:
        self.arr.append(num)
        self.count += 1
        if self.count > self.k:
            
            self.dic[self.arr[self.left]] -= 1
            
            if  self.dic[self.arr[self.left]] <= 0:
                del  self.dic[self.arr[self.left]]
            
            self.left+=1
    
        self.dic[num] += 1
        if len(self.dic) != 1 or self.dic[self.value] != self.k:
            
            return False
        else:
            return True 
            
        
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)