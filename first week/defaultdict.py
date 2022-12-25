# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m = list(map(int,input().split()))

c = defaultdict(list)
for _ in range(1,n+1):
    c[input()].append(str(_))
for _ in range(m):
    h = input()
    if h in c:
        print(" ".join(c[h]))
    else:
        print(-1)
