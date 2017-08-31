contador=0
def minimo(array):
    a=array
    global contador
    resultado=-1
    for i in range(0,len(array)):
    	esminimo=True
    	for j in range (0,len(a)):
    		contador+=1
    		if array[i]>array[j]:
    			esminimno=False
    			break
    		if esminimo:
    			resultado=i
    			break
    		else:
    			a=array
    	return resultado

def ordenar(array):
    a=array
    resultado=[]
    for i in range(0,len(array)):
    	m=minimo(a)
    	resultado.append(a[m])
    	del a[m]
    return resultado

import random
p=random.sample(range(2,102),2)
contador=0
 
print(p)
print(p[minimo(p)])
print(min(p))
print(ordenar(p))
print(contador)
