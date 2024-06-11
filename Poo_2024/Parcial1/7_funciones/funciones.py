"""""
#una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un porograma mas pequeño que cumple una funcion especifica. la funcion se puede reutilizar con el simple hecho de invocarla es decir mandarla llamar.

#sitanxis

def nombredeMifucion (parametros):
     bloque o conjunto de instrucciones

nombredeMifucion (parametros)

#Las funciones pueden ser 4 tipos 
#1°-funcion que no recibe parametros y no regresa valor 
#2°-funcion que no recibe parametros y regresa valor 
#3°-funcion que recibe parametros y no regresa valor
#4°-funcion que recibe parametros y regresa valor 


#Ejemplo 1: crear una funcion para imprimir nombres de personas 

#1°-funcion que no recibe parametros y no regresa valor 
def solicitarNombres():
    nombre=input("ingresa el nombre completo: ")
solicitarNombres()

#ejemplo 2:suma dos numeros 
def suma():
    n1=int(input("numero #1. "))
    n2=int(input("numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma ()

#ejemplo 3:suma de dos numeros 
#2°-funcion que no recibe parametros y regresa valor 

def suma():
    n1=int(input("numero #1. "))
    n2=int(input("numero #2: "))
    suma=n1+n2
    return suma

resultado_suma=suma()
print(f"la suma es: {resultado_suma}")
suma ()

#ejemplo 4:suma de dos numeros 
#3°-funcion que recibe parametros y no regresa valor

def suma(num1,num2):
    suma=num1+num2
    print(f"la suma es: {suma}")

num1=int(input("numero #1. "))
num2=int(input("numero #2: "))
suma(num1,num2)

#ejemplo 5:suma de dos numeros 
#4°-funcion que recibe parametros y regresa valor 

def suma(num1,num2):
    suma=num1+num2
    return suma 
    print(f"la suma es: {suma}")

num1=int(input("numero #1. "))
num2=int(input("numero #2: "))
resultado_suma=suma(n1,n2)
print(f"la suma es: {suma}")

#ejemplo 6: Crear un programa que solicite a travez de una funcion la siguiente informacion: nombre del paciente, edad, estatura, tipo de sangre. Utilizar los 4 tipos de funciones. 
"""""

#una función es un conjunto de instrucciones agrupadas bao un nombre en particulas como un programa más pqueño que comple una función especifica, la función se puede reutilizar con el simple hecho de incovarla es decir mandarla a llamar

#Sintaxis:
def nombredeMiFuncion():
    #bloque o conjunto de intrucciónes
    print("bloque o conjunto de intrucciónes")

nombredeMiFuncion()

#las funciones puedes ser de 4 tipos
#1.- Funciones que no reciben parametros y no regresa valor
#2.- funciones que no recibe parametro y regresa valor
#3.- funciones que no recibe parametro y NO regresa valor
#4.- funciones que recibe parametro y regresa valor

#Ejemplo 1 - crear una función para imprimir nombres de personas
def solicitarNombre():
    nombre=input("Ingresa el nombre completo: ")

solicitarNombre()

#Ejemplo 2 - Realizar sumatoria (No recibe parametro pero regresa valor)
def suma():
    n1=int(input("Número #1: "))
    n2=int(input("Número #2: "))
    suma = n1+n2
    print(f"La suma de los números es {suma}")

suma()


#Ejemplo 3 - Sumar números (No recibe parametro pero regresa valor)

def suma():
    n1=int(input("Número #1: "))
    n2=int(input("Número #2: "))
    suma = n1+n2
    return suma

resultado_suma=suma()
print(f"La suma de los números es {suma()}")
print(f"La suma de los números es {resultado_suma}")


#Ejmplo 4 - Realizar suma
#funciones que recibe parametro y NO regresa valor

def suma(n1,n2):
    suma = n1+n2
    print(suma)

n1=int(input("Número #1: "))
n2=int(input("Número #2: "))
suma(n1,n2)


#Ejmplo 5 - Realizar suma
#funciones que recibe parametro y regresa valor 

def suma(n1,n2):
    suma = n1+n2
    return suma

n1=int(input("Número #1: "))
n2=int(input("Número #2: "))
suma(n1,n2)



#Ejemplo - Tarea
#Crear un programa que solicite a traves de una función la siguiente información
#Nombre de paciente
#Edad
#Estatura
#Tipo de sangre
#Utilzar los 4 tipos de funciónes

def infoPaciente():
    nombre = input("Escribe el nombre del paciente")
    edad = input("Escribe la edad del paciente")
    eatatura = input("Escribe la  estatura del paciente")
    tipoSangre = input("Escribe el tipo de sangre del paciente")
    return(f"Nombre: ")


valor= infoPaciente()
#Recibe parametros pero no regresa valor
def infoPaciente2(nom, edad, est, sandre):
    return