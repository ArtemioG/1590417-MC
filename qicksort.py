import random
cnt=0

def quicksort(arr):
    global cnt
    if len(arr)<=1:
        return arr
    p=arr.pop(0)
    menores,mayores=[],[]
    for e in arr:
        cnt+=1
        if e<=p:
            menores.append(e)
        else:
            mayores.append(e)
    return quicksort(menores)+[p]+quicksort(mayores)

a=[123,45,1,2300,-12,1,-6]
print(a)
quicksort(a)
