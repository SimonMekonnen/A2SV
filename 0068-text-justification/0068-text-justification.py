class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ans = []
        left = 0
        total = 0
        for right in range(len(words)):
            total += len(words[right]) + 1
            if total - 1 > maxWidth:
                ans.append(words[left : right])
                left = right
                total = len(words[right]) + 1
    
        ans.append(words[left : ])
        total = []
        for i in range(len(ans) - 1):
            t = 0
            todo = []
            for j in ans[i]:
                t += len(j)
                todo.append(list(j))
            
            now = maxWidth - t
            n = 0
        
            while now != 0 and len(todo)!=1:
                n%=(len(todo) - 1)
                todo[n].append(" ")
                now-= 1
                n+=1
            if len(todo) == 1:
                todo[0].extend([" " for i in range(now)])
            total.append(todo)
        t = 0
        for i in range(len(ans[-1])):
            t += len(ans[-1][i])
            ans[-1][i] = list(ans[-1][i])
        now = maxWidth - t
        for i in range(len(ans[-1]) - 1):
            ans[-1][i].append(" ")
            now -= 1
        ans[-1][-1].extend([" " for i in range(now)])
        total.append(ans[-1])
             
        for i in range(len(total)):
            for j in range(len(total[i])):
                total[i][j] = "".join(total[i][j])
            total[i] = "".join(total[i])
            
        
        return total
                
                
                    
                
                
                
            
                
                
            
        
        
            
        