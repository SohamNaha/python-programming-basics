def intreverse(n):
	temp = n
	reverse = 0
	while temp>0 :
		x = temp%10
		reverse = reverse*10 + x
		temp = temp//10
	return(reverse)

from isprime import *

def sumprimes(l):
	sum = 0
	for i in l:
		if isprime(i):
			sum = sum + i
	return(sum)


#from pythonds.basic.stack import stack
#def matched(symbolString):
	#s = Stack()
	#balanced = True
	#index = 0
	#while index<len(symbolString):
		#symbol = symbolString[index]
		#if symbol == "(":
			#s.push(symbol)
		#else:
				#if symbol == ")":
					#s.pop()
				#if s.isEmpty():
					#balanced = True
		#index = index+1
	#if balanced and s.isEmpty():
		#return True
	#else :
		#return False
