cnt=0
def primo(n):
    global cnt
    for i in range(2, n):
        cnt+=1
        if ((n%i)==0):
            return ("No es primo")
    return ("Es primo")

for i in range (2,50): 
	cnt=0
	print(i,primo(i),cnt)
