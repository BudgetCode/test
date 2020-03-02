array = list(map(int,input().split()))
n = int(input())
length = len(array)
left,result = [],[]
x = 1
left.append(x)
for i in range(1,length):
    x *= array[i-1]
    left.append(x)
x = 1
result.append(x*array[length-1])
for i in range(length-1,0,-1):
    x *= array[i]
    result.insert(0,x*left[i-1])
print(result[n])
