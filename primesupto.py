from isprime import *
def primesupto(n):
	primelist = []
	for i in range (1,n+1):
		if isprime(i):
			primelist.append(i)
	return(primelist)