#los errores de ejecucion en un lenguaje de programacion se presentan cuando existe una anomalia dentro de laa ejecucion del codigo la cual provoca que se detenga la ejecucion del codigo lo cual provoca que se detenga la ejecucion del SW con el control y manejo de exepciones sera posible minimizarlo o evitar la interrupcion del programa debido a una excepcion.

#ejemplo 1: cuando una variable no se genera 
try:
    nombre=input("introduce el nombre completo de una persona: ")
    if len(nombre)>0:
        nombre_usuario="el nombre completo del usuario es: "+nombre

    print(nombre_usuario)

except:print("es necesario introducir un nombre de usuario...verifica por favor")

#ejemplo 2: cuando se solicita un numero y se ingresa otra cosa

try: 
  numero=input("ingrese un numero entero: ")
  if numero>0:
    print("soy un numero positivo")
  elif numero==0:
    print("soy un numero entero neutro")
  else: 
    print("soy un numero entero negativo")
except ValueError:
   print("introduce un valor numerico entero")

#ejemplo 3: generan multiples excepciones 

try: 
   numero=int(input("introduce un numero: "))
   print("el cuadrado del numero es: "+str(numero*numero))
except ValueError:
   print("introduce un valor numerico entero")
except TypeError:
   print("se debe convertir el numero a entero")
else:
   print("no se presentaron errores de ejecucion")
finally:
   print("termine la operacion")
   