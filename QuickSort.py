def QuickSort(A,l,r):
	if r-l<=1:			# Base Condition
		return()
	# Partition with respect to pivot, A[l]
	yellow = l+1
	for green in range (l+1,r):
		if A[green]<=A[l]:
			(A[yellow],A[green]) = (A[green],A[yellow])
			yellow = yellow+1
	# Move pivot into place
	(A[yellow-1],A[l])=(A[l],A[yellow-1])
	# recursive calls
	QuickSort(A,l,yellow-1)
	QuickSort(A,yellow,r)
