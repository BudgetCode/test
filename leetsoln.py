array = list(map(int,input().split()))
n = int(input())
left,right = [],[]
x = 1
left.append(x)
for i in range(1,len(array)):
    x *= array[i-1]
    left.append(x)
x = 1
right.append(x)
for i in range(len(array)-1,0,-1):
    x *= array[i]
    right.insert(0,x)

print(left[n]*right[n])
