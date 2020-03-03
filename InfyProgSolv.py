"""
take an input say (12630). Find out all the numbers in this input which were a multiplication of consecutive numbers. It included 2(1*2), 6(2*3), 12(3*4), 30(5*6).
"""

strNum = input()
number = int(strNum)
x = count = 0
nRes = dict()
for i in range(1,number):
	x = i*(i+1)
	if x > number or count >= 2: break
	x = str(x)
	if x in strNum: nRes[x] = (i,i+1)
	else: count +=1
print(nRes)
