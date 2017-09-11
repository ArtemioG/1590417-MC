def selection(arr):
	for i in range(0,len(arr)-1):
		val=i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[val]:
				val=j
		if val!=i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return arr

A=[56,3,21,7,105,-7,4506,0,0]
print(A)
selection(A)