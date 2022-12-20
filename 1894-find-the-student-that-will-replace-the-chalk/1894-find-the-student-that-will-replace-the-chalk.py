class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        pre = []
        total = 0
        for i,n in enumerate(chalk):
            total+=n
            if total > k:
                return i 
            pre.append(total)
        k%=pre[-1]
        for i,n in enumerate(pre):
            if n > k:
                return i
        
            
        

            
            
        