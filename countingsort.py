def countingSort(arr):
    count = [0]*100
    print(len(count))
    for i in arr:
        print(i)
        count[i]+=1
    return count