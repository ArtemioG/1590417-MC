def burbuja(array):
    cnt=0
    for i in range(0,len(array)-1):
        for j in range (0,len(array)-1):
            cnt+=1
            if (array[j+1])<array[j]:
                array[j],array[j+1]=array[j+1],array[j]
    return cnt

def insercion(array):
    cnt=0
    for indice in range (1,len(array)):
        valor=array[indice]
        i=indice-1
        while i>=0:
            cnt+=1
            if valor<array[i]:
                array[i+1]=array[i]
                array[i]=valor
                i-=1
            else:
                break
    return cnt

def selection(array):
    cnt=0
    for i in range(0,len(array)-1):
	    val=i
	    for j in range(i+1,len(array)):
	    	if array[j]<array[val]:
    			val=j
    	    cnt+=1
	    if val!=i:
		    aux=array[i]
		    array[i]=array[val]
		    array[val]=aux
    return cnt


def quicksort(array):
    cnt=0
    if len(array)<=1:
        return array
    p=array.pop(0)
    menores,mayores=[],[]
    for e in array:
        cnt+=1
        if e<=p:
            menores.append(e)
        else:
            mayores.append(e)
    return cnt

import random
def randomarray(array):
    a=[]
    for i in range(array):
        a.append(random.randint(0,array))
    return a

import copy
lonarr=10
while lonarr<1000:
    for i in range(1,30):
        arreglo=randomarray(lonarr)
        aa,ab,ac,ad = copy.deepcopy(arreglo),copy.deepcopy(arreglo),copy.deepcopy(arreglo),copy.deepcopy(arreglo)
        bsort=burbuja(aa)
        isort=insercion(ab)
        ssort=selection(ac)
        qsort=quicksort(ad)
        print(lonarr,bsort,isort,ssort,qsort)
    lonarr*=2
