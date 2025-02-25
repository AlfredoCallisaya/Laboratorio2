#Programacion Funcional
#Dada una lista de numeros, filtrar los pares y luego calcular el cuadrado de cada uno 
numeros=[1,2,3,4,5,6,7,8,9,10]
pares_cuadrados = list(map(lambda x: (x**2)+1,
filter(lambda x: x % 2 !=0, numeros)))
print ("Cuadrados de los numeros pares: ", pares_cuadrados)