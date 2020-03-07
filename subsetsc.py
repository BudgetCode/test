n = int(input())
array = list(map(int,input().split()))

from itertools import chain, combinations
x = len(array)
x = [[array[j] for j in range(x) if (i & (1 << j))] for i in range(1<<x)][1:]
n =  [m for m in x if len(list(filter(lambda y:(y<0),m)))%2 != 0] # list of all the valid subsets with odd no. of negatives
sn = len(n)
print(sn)
