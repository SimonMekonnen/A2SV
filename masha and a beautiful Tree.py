N = int(input())
for _ in range(N):
    c = int(input())
    nums = list(map(int,input().split()))
    count = 0
    def merge(l,r):
        global count
        if l == r:
            return [nums[l]]
        
        mid = (l + r) //2 
        left = merge(l,mid)
        right = merge(mid + 1,r)
        if left[-1] > right[0]:
            count += 1
            return right + left
        else:
            return left + right
    result = merge(0,len(nums) - 1)
    if sorted(nums) == result:
        print(count)
    else:
        print(-1)
            
        
        
        
