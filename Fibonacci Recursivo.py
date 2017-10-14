cnt=0
def fibonacciR(n):
	global cnt
	cnt+=1
	if n==0 or n==1:
		return (1) 
	else:
		return fibonacciR(n-2)+fibonacciR(n-1)

for i in range (2,40): 
	cnt=0
	print(i,fibonacciR(i),cnt)
