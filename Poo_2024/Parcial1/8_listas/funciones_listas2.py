paises=["Mexico","USA","Brasil","Japon"]
numeros=[23,100,3.1416,0.100]
varios=["hola",True,100,10.22]

#ordenar la lista

print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#agregar elementos
print(numeros)
numeros.insert(len(numeros),100)
print(numeros)
numeros.append(100)

#eliminar elementos
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(100)

#buscar dentro de una lista un valor o un dato 

encontrar="Brasil"in paises
print(encontrar)

#dar la vuelta 
print(varios)
varios.reverse()
print(varios)

#unir listas
print(paises)
paises.extend(numeros)
print(paises)

#vaciar una lista 
print(varios)
varios.clear()
print(varios)

