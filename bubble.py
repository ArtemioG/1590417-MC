def burbuja(array):
    for i in range(0,len(array)-1):
        for j in range (0,len(array)-1):
            if (array[j+1])<array[j]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

A=[50,12,23,5,6,42,81]
burbuja(A)
