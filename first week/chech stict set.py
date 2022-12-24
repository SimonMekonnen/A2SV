# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())

while n > 0:
    c = set(map(int,input().split()))
    ans = True
    for i in c:
        if len(c)>=len(A) or i not in A:
            ans = False
    if not ans: 
        break
    n-=1
print(ans)
        