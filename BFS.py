class Fila:
    def __init__(self):
        self.fila=[]
    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

class Grafo:
    def __init__(self):
        self.V = set() #Un conjunto
        self.E = dict() #Un mapeo de pesos de aristas
        self.vecinos = dict() #Un mapeo

    def agrega(self,v):
        self.V.add(v)
        if not v in self.vecinos: #vecindad de v
            self.vecinos[v] = set() #Inicialmente no tiene nada

    def conecta(self,v,u,peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v,u)]=self.E[(u,v)]=peso #En ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)

    def complemento(self):
        comp=Grafo()
        for v in self.V:
            for w in self.V:
                if v!=w and (v,w) not in self.E:
                    comp.conecta(v,w,1)
        return comp

def BFS(g,ni): 
    visitados=[]
    f=Fila()
    f.meter(ni)
    while(f.longitud>0):
        na=f.obtener()
        visitados.append(na)
        ln=g.vecinos[na]
        for nodo in ln:
            if nodo not in visitados:
                f.meter(nodo)
    return visitados

prueba=Grafo()
prueba.conecta('a','b')
prueba.conecta('c','a')
prueba.conecta('d','b')
BFS(prueba,'a')
BFS(prueba,'b')
prueba.E
prueba.V
