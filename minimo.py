import random
a = []
for i in range(100):
	a.append(i)

def minimo(arreglo):
	auxiliar = arreglo # creo un arreglo auxiliar
	resultado = 0
	for a1 in arr: # para cada elemento a1 del arreglo/conjunto
		auxiliar.pop(a1) # remuevo a1 del conjunto auxiliar
 		for a2 in auxiliar: # para cada elemento a2 del conjunto auxiliar auxiliar
			print (a1,a2)
			if(a1 > a2): #comparo si a1 es mayor que a2
				break #si lo es, salgo para probar el siguiente a1, si no, comparo a1 con el siguiente a2
		resultado = a1
		break
	return resultado


random.shuffle(a)
