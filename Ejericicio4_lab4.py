#Programa con dos pilas 
class Cola_con_pilas:
    def __init__(self):
        self.pila_ent = []
        self.pila_sal = []

    def enqueue(self, ele):
        self.pila_ent.append(ele)
    
    def dequeue(self):
        if not self.pila_sal:
            if not self.pila_ent:
                return None
            while self.pila_ent:
                self.pila_sal.append(self.pila_ent.pop())
        return self.pila_sal.pop()
    
    def vacia(self):
        return not (self.pila_ent or self.pila_sal)

def ingresar_elementos(cola):
    while True:
        elemento = input("Ingrese un elemento para agregar a la cola (o 'fin' para terminar): ")
        if elemento.lower() == 'fin':
            break
        cola.enqueue(elemento)

cola = Cola_con_pilas()
ingresar_elementos(cola)

while not cola.vacia():
    print("Desencolando:", cola.dequeue())
print("La cola está vacía?", cola.vacia()) 
