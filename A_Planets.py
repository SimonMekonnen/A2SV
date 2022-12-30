from collections import Counter


N = int(input())
for _ in range(N):
    n, c = list(map(int, input().split()))
    dic = Counter(map(int, input().split()))
    
    ans = 0
    
    for i in dic:
        
        if dic[i] < c:
            ans+=dic[i]
        else:
            ans+=c
            
    print(ans)
            