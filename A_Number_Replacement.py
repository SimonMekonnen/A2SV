from collections import defaultdict


N  = int(input())
for _ in range(N):
    n = int(input())
    num = list(map(int,input().split()))
    s = input()
    dic = {}
    d  = ""
    for i in range(n):
        if num[i] not in dic:
            dic[num[i]] = s[i]
    for i in range(n):
        d+=dic[num[i]]
    
    if d == s:
        print("YES")
    else:
        print("NO")
    
    
            