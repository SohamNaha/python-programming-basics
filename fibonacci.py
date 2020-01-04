def fib(n):
	if fibtable[n]:
		return(fibtable[n])
	if n==0 and n==1:
		value = n
	else :
		value = fib(n-1)+fib(n-2)
	fibtable[n] = value
	return(value)

def fibdyn(n):
	fibtable[0]=0
	fibtable[1]=1
	for i in range(2,n+1):
		fibtable[i] = fibtable[i-1] + fibtable[i-2]
	return (fibtable[n])