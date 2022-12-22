# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
while n > 0:
    k = input()
    arr = list(map(int,input().split()))
    var = max(arr[0],arr[-1])
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] > arr[right]:
            if arr[left] > var:
                print("No")
                break
            var = arr[left]
            left+=1
           
        else:
            if arr[right] > var:
                print("No")
                break
            var = arr[right]
            right-=1
    if left >= right and arr[left] <= var:
        print("Yes")
    n-=1