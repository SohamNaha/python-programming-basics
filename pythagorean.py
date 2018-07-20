def PythagoreanTriples(l,m,n):
	return([(x,y,z) for x in range(1,l) for y in range(x,m) for z in range(y,n) if x*x+y*y==z*z])
