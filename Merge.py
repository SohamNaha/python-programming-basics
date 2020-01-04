def Merge(a,b):
	(c,m,n) = ([],len(a),len(b))
	(i,j) = (0,0)
	while (i+j)<(m+n):
		if i==m :    	#case 1: if a is empty
			c.append(b[j])
			j=j+1
		elif j==n : 		#case 2: if b is empty
			c.append(a[i])
			i=i+1
		elif a[i]<=b[j]:	#case 3: if head of a is smaller
			c.append(a[i])
			i=i+1
		elif a[i]>b[j]:		#case 4: if head of b is smaller
			c.append(b[j])
			j=j+1
	return(c)
