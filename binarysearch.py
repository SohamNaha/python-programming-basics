def binarysearch(seq,v,l,r):
	#search for v in seq[l:r],sequence is sorted
	if (r-l)==0:
		return(False)
	mid =int((l+r)/2)
	if seq[mid]==v :
		return (True)
	elif v<seq[mid] : 
		return(binarysearch(seq,v,l,mid))
	elif v>seq[mid] :
		return(binarysearch(seq,v,mid+1,r))