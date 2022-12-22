# Enter your code here. Read input from STDIN. Print output to STDOUT
l = input()
arr = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
ans = 0
for i in arr:
    if i in A:
        ans+=1
    elif i in B:
        ans-=1
print(ans)
    