cnt=0
def orden_por_insercion(array):
    global cnt
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
    return array

a=[67,40,12,83,23,678,9000,12]
print(a)
orden_por_insercion(a)
