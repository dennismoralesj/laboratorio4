#Verificación de Paréntesis Balanceados:

def parentesis_balanceados(cadena):
    pila = []  
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter)  
        elif caracter == ')':
            if not pila:  
                return False
            else:
                pila.pop()  
    return len(pila) == 0 

cadena = input("Ingrese la cadena de paréntesis: ")

if parentesis_balanceados(cadena):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")
