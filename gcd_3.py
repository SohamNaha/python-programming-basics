def gcd(m,n):
	for i in range(1,min(m,n)):	
		if (m%i)==0 and (n%i)==0:
			mrcf = i
	return(mrcf)


N = int(input())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

sum_list = []

for i in range(N):
    
	for j in range(i,N):
        
		gcd1 = gcd(A[i],A[j])
        
		gcd2 = gcd(B[i],B[j])    
        
		sum_gcd = gcd1 + gcd2
        
		sum_list.append(sum_gcd)

		print(sum_list,end=' ')	
		

x = max(sum_list)

y = sum_list.count(x)
print(x,end=' ')

print(y)