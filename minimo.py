Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> contador=0
>>> def minimo(array):
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

	
>>> def ordenar(array):
	a=array
	resultado=[]
	for i in range(0,len(array))
	
SyntaxError: invalid syntax
>>> def ordenar(array):
	a=array
	resultado=[]
	for i in range(0,len(array)):
		m=minimo(a)
		resultado.append(a[m])
		del a[m]
	return resultado

>>> import random
>>> p=random.sample(range(2,102),2)
>>> contador=0
>>> 
>>> print(p)
[76, 96]
>>> print(p[minimo(p)])
76
>>> print(min(p))
76
>>> print(ordenar(p))
[76, 96]
>>> print(contador)
3
>>> 
