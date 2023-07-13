#User function Template for python3
from collections import deque
class Solution:
    def findOrder(self,dic, N, K):
        graph = [[] for i in range(26)]
        degree = [0 for i in range(26)]
        present = set()
        for i in range(N - 1):
            first = dic[i]
            second = dic[i + 1]
            a = 0
            while a < len(first) and a < len(second) and first[a] == second[a]:
                a += 1
            
            if a < len(first) and a < len(second):
                graph[ord(first[a]) - ord('a')].append(ord(second[a]) - ord('a'))
                degree[ord(second[a]) - ord('a')] += 1
    
        for i in dic:
            for j in i:
                present.add(j)
        que = deque()
        for i in range(len(degree)):
            if degree[i] == 0 and chr(i + ord('a')) in present:
                que.append(i)
 
        ans = ""
    
        while que:
            cur = que.popleft()
            ans += chr(ord('a') + cur)
            for neigh in graph[cur]:
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    que.append(neigh)
       
  
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
