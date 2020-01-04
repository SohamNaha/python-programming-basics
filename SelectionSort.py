def SelectionSort(l):
	#scan slices l[0:len(l)], l[1:len(l)]
	for start in range(len(l)):
		minpos = start
		#find minimum value in slice
		for i in range(minpos,len(l)):
			if l[i]<l[minpos]:
				minpos = i
		#.... and move it to start of slice
		(l[start],l[minpos]) = (l[minpos],l[start])