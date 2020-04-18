def factorial_num(num):
	fac = 1
	while num > 0:
		fac = fac * num
		num -=1
	return(fac)
	
resilt = factorial_num(4)
print(resilt)