# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

a = int(input())

c = list(map(int,input().split()))
c = collections.Counter(c)

print(min(c,key = lambda x:c[x]))
