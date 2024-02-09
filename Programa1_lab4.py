#Implementación de una Pila (Stack)
def pila_dada(lista): #define la función "pila_dada" y la convierte en lista
    pila = []  #se inicializa pila con un valor vacio
    print('La Pila Ha Sido Añadida:')
    for elem in lista: #esta sirve para recorrer cada elemento que fue ingresado
        print(f'El elemento "{elem}" nuevo entrando a la Pila')
        pila.append(elem)  #sive para agregar el elemento al final de la fila
    print(pila)  #imprime la pila completa agregada

    print("\nEliminando elementos de la pila:")
    while pila:
        elemento = pila.pop()  #esta toma y elimina el ultimo elemento de la pila 
        print(f'Elemento "{elemento}" eliminado')
        print(pila)  

    print("\nLista Inversa:")
    print(lista[::-1]) #esta imprime la lista invertida 

lista = input("Ingrese la lista separada por espacios: ").split()
pila_dada(lista)

