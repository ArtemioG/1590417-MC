from heapq import heappop, heappush

def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
        dist = dict() #diccionario de distancias 
        visited = set() #Conjunto de visitados
        while len(q) > 0: #mientras exista un nodo pendiente
            (l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
            if u not in visited: # si no lo hemos visitado
                visited.add(u) #se agrega a visitados
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	#agrega al diccionario
            p = (u, p) #Tupla del nodo y el camino
            for n in self.vecinos[u]: #Para cada hijo del nodo actual
                if n not in visited: #si no lo hemos visitado
                    el = self.E[(u,n)] #se toma la distancia del nodo acutal hacia el nodo hijo
                    heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
        return dist #regresa el diccionario de distancias

g=Grafo()
g.conecta('q','a',3)
g.conecta('q','e',6)
g.conecta('q','i',9)
g.conecta('q','m',12)
g.conecta('q','q',15)
g.conecta('q','u',18)
g.conecta('q','y',21)
g.conecta('y','b',24)
g.conecta('y','f',27)
g.conecta('y','j',30)
g.conecta('y','n',2)
g.conecta('y','r',4)
g.conecta('y','v',6)
g.conecta('y','c',8)
g.conecta('s','g',10)
g.conecta('s','k',12)
g.conecta('s','o',14)
g.conecta('s','s',16)
g.conecta('s','w',18)
g.conecta('s','d',20)
g.conecta('s','h',30)
g.conecta('x','l',27)
g.conecta('x','p',24)
g.conecta('x','t',21)
g.conecta('x','x',18)
g.conecta('x','c',15)
g.conecta('x','b',12)
g.conecta('x','a',9)
g.conecta('u','f',6)
g.conecta('u','e',3)
g.conecta('u','l',20)
g.conecta('u','k',18)
g.conecta('u','j',16)
g.conecta('u','i',14)
g.conecta('u','p',12)
g.conecta('w','o',10)
g.conecta('w','v',8)
g.conecta('w','u',6)
g.conecta('w','t',4)
g.conecta('w','s',2)
g.conecta('w','r',1)
g.conecta('w','d',5)
g.conecta('w','h',7)
g.conecta('v','g',11)
g.conecta('v','n',13)
g.conecta('v','m',17)
g.conecta('v','q',23)
g.conecta('v','y',29)
g.conecta('v','x',3)
g.conecta('v','w',1)



print(g.shortest('v'))

