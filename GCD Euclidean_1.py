#from the nptel course the first program that was probably used was GCD algorithm used my Euclid.
#in this euclid said that if there are two numbers m and n(m>n) and we need to find their gcd then if m/n=0 then n is a divisor of m, and hence the gcd is n.
#if that is not the case then find their difference(m-n) (actually the remainder) and perform it recursively



def gcd(m,n):
	if m<n:
		(m,n) = (n,m)       #if m<n then swaps m and n values
	if (m%n)==0:
		return (n)          #if n is a divisor of m, return n
	else : 
		diff = m-n
		return(gcd(max(n,diff),min(n,diff)))
