class Solution:
    def insert(self, inte: List[List[int]], new: List[int]) -> List[List[int]]:
        
        interval = []
        answer = []
        ip = 0
        np = 0
        while np!=1:
            if ip < len(inte) and inte[ip][0] < new[0] or np == 1:
                    interval.append(inte[ip])
                    ip+=1
            else:
                    interval.append(new)
                    np = 1
        interval += inte[ip:]
            
        for i in interval:
            
            if answer and answer[-1][1] >= i[0]:
                c = answer.pop()

                answer.append([c[0],max(c[1],i[1])])
            
            else:
                
                answer.append(i)
                
        return answer
               
                
                
                
                
                    
                    
                
                
        
        
        