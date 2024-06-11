"""
list(array)
son colecciones o cinjunto de datos/valores bajo un mismo nombre,para acceder 
a los valores se hace como un indice numerico

#NOTA: sus valorez si son modificables 

"""

#CREAR UNA LISTA DE NUMEROS E IMPRIMIR EL CONTENIDO:

numeros=[23,34]
print(numeros)

#recorrer la lista con ciclo for 
for i in numeros:
    print(i)

#recorrer la lista con ciclo while
i=1
while i<=len(numeros):
    print(numeros)
     
#ejemplo 2: crear una lista de palabras y posteriormente 
#buscar la coincidencia de una palabra 

palabras=["naranja","utd","america","azul"]

palabra_buscar=input("ingresa la palabra a buscar: ")

for i in palabras:
    if i==palabra_buscar:
        print(f"se encontro la palabra a buscar en la posicion")

numeros[23,34,23]
print(numeros)

#agregar un elemento
numeros.append(100)
print(numeros)
numeros.insert(3,200)
print(numeros)

#eliminar un elemento
numeros.remove(100) # indicar el elemento a borrar 
print(numeros)
numeros.pop(2) #indicar la posicion del elemento a borrar
print(numeros)
