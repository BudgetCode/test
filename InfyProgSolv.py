
"""
take an input say (12630). Find out the longest sequence numbers in this input which were a multiplication of consecutive numbers. It included 2(1*2), 6(2*3), 12(3*4), 30(5*6).
"""

from math import sqrt ,ceil ,floor

strNum = input()
count = iter = 0
array = []
result = [dict()]

for i in range(len(strNum)):
	for n in range(i+1,len(strNum)+1):
		array.append(strNum[i:n])

array = list(map(int,array))
array.sort()

for i in array[2:]:
	root = sqrt(i)
	x = ceil(root)
	y = floor(root)
	if x==y:continue
	if x*y in array:
		if count >= 2:
			count =0
			iter +=1
			result.append(dict())
		result[iter][x*y] = y,x
	else:count+=1

print(max(result,key=lambda x:len(x)))



"""
#Slower than above code

from math import sqrt ,ceil

strNum = input()
number = ceil(sqrt(int(strNum)))
x = count = iter = 0
nRes = [dict()]
for i in range(1,number):
	x = i*(i+1)
	x = str(x)
	if x in strNum:
		if count >= 2:
			count = 0
			iter+=1
			nRes.append(dict())
		nRes[iter][x] = (i,i+1)
	else: count+=1

print(max(nRes,key=lambda x:len(x)))
"""
