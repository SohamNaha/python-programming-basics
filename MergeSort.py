from Merge import *
def MergeSort(a,l,r):
	if r-l<=1:					#Base condition
		return(a[l:r])
	mid = (l+r)//2				#Recursion
	L = MergeSort(a,l,mid)
	R = MergeSort(a,mid,r)
	return(Merge(L,R))			#Recomposition