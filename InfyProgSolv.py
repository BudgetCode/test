"""
take an input say (12630). Find out all the numbers in this input which were a multiplication of consecutive numbers. It included 2(1*2), 6(2*3), 12(3*4), 30(5*6).
"""

number , x = int(input()) , 0
strNum = str(number)
nRes = dict()
for i in range(1,number):
	x = i*(i+1)
	if x > number: break
	x = str(x)
	if x in strNum: nRes[x] = (i,i+1)
print(nRes)