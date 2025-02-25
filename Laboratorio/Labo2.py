#Programacion funcional
    #Funciones puras
    #Inmutabilidad
    #Funciones de orden superior
#Dado un numero n que nos muestre cual seria el factorial
def Factorial(n):
    resultado= 1
    for i in range (1, n+1):
        resultado *=i
    return resultado
numero= int (input("Ingrese un numero para caluclar su fatorial: "))
print(f"El fatorial del {numero} es: {Factorial(numero)}")

