#Pila la mitad ordenada normal y la otra invertida 
class Queue:
    def __init__(self):
        self.items = []   # Inicializa la lista vacía

    def enqueue(self, item):
        self.items.append(item)   # Agrega un elemento a la cola

    def dequeue(self):
        if not self.is_empty():  # Verifica si la cola no está vacía
            return self.items.pop(0)  # Quita y devuelve el primer elemento de la cola
        else:
            return None  # Si la cola está vacía, devuelve None

    def is_empty(self):
        return len(self.items) == 0  # Devuelve True si la cola está vacía, False en caso contrario

    def size(self):
        return len(self.items)  # Devuelve el tamaño de la cola
    
def reversa(queue):
    stack = [] # Se inicializa una lista vacía llamada stack, que actuará como una pila.
    size = queue.size() # Se obtiene el tamaño de la cola.
    half_size = size // 2 # Se calcula la mitad del tamaño de la cola.

    for _ in range(half_size):
        stack.append(queue.dequeue()) # Se desencolan y se agregan a la pila los primeros elementos de la cola, hasta la mitad.

    while stack:
        queue.enqueue(stack.pop()) # Se desapilan los elementos de la pila y se vuelven a encolar en la cola.

def ingreso_datos():
    queue = Queue() #funcion para ingresar datos a la lista 
    n = int(input("Ingrese la cantidad de elementos en la cola: "))
    for i in range(n): #contador ingresado por el usuario y hasta ahi llegara el ciclo
        item = input(f"Ingrese el elemento {i + 1}: ")
        queue.enqueue(item) #agraga los datos a la pila
    return queue

if __name__ == "__main__":
    queue = ingreso_datos() #llama la función de ingreso de datos 
    print("Cola original:", queue.items)  #Imprime pila original ingresada

    reversa(queue) #llama la funcion de datos en reversa
    print("Cola con la mitad de elementos revertidos:", queue.items) #imprime la cola revertida