"""
take an input say (12630). Find out all the numbers in this input which were a multiplication of consecutive numbers. It included 2(1*2), 6(2*3), 12(3*4), 30(5*6).
"""
strNum = input()
number = int(strNum) 
x = count = iter = 0
nRes = [dict()]
for i in range(1,number):
	x = i*(i+1)
	if x > number: break
	x = str(x)
	if x in strNum:
		if iter >= 2:
			iter = 0
			count+=1
			nRes.append(dict())
		nRes[count][x] = (i,i+1)
	else: iter+=1

print(max(nRes,key=lambda x:len(x)))
