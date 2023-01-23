from collections import defaultdict


N = int(input())
for _ in range(N):
    n,k = list(map(int,input().split()))
    nums = []
    table1 = defaultdict(int)
    table2 = defaultdict(int)
    for i in range(n):
        nums.append(list(map(int,input().split())))
    for row in range(n):
        for col in range(k):
            table1[col - row]+=nums[row][col]
            table2[col + row] += nums[row][col]
    ans = 0
    for row in range(n):
        for col in range(k):
            ans = max(ans,table1[col - row] + table2[col + row] - nums[row][col])
    print(ans)
