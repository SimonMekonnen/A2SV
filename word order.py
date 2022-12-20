# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections 
n = int(input())
ans = []
for i in range(n):
    ans.append(input())
    
c = collections.Counter(ans)

print(len(set(ans)))

z = [str(i) for i in c.values()]

print(" ".join(z))