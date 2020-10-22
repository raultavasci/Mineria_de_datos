import pandas as pd 
import numpy as np


# Tuplas
# Crear una variable flotante, integer, boleana y compleja e imprimir el tipo de variable que es.
a =2.1
b = 1
c=True
d=2.23j
x=a,b,c,d
for i in x:
	print("This is a",type(i)," variable")

# Crear una tupla con valores enteros imprimir el primer y ultimo valor.
A = (1,2,3,4,5,6)
print("Primer valor tuple: ",A[0],"\nultimo valor",A[-1])

# Añadir 3 valores de string a la tupla.
B = ("a","b","c")
C = A+B
print(C)

# Verificar si una variable existe dentro de la tupla.
print(isinstance(C,list),"\n",isinstance(C,tuple))

# Listas
# Crear una lista con 40 elementos aleatorios enteros.
import random
randomlist = []
for i in range(0,40):
	n = random.randint(1,40)
	randomlist.append(n)
print("Lista generada:\n",randomlist)
print("\nLargo de lista: \n",len(randomlist),"\n\n")
# Con una funcion (def) crear dos listas nuevas a partir de la lista creada por numeros aleatorios, en la cual en una esten los elementos pares, y en la otra los elementos impares.
def list(randomlist):
    im=[]
    p=[]
    for i in range(len(randomlist)):
        if randomlist[i]%2==0:
            p.append(randomlist[i])
        else:
            im.append(randomlist[i])
    return p,im
p,im=list(randomlist)
print("Pares",p,"\nImpares",im)
# Crear dos variables con la longitud de ambas listas nuevas e imprimir las variables.
Par = len(p)
imp = len(im)
print("Longitud de pares: ",Par,"\nLongitud de impares: ",imp)

# Ordenar los elementos de la lista par de mayor a menor, y los de la lista impar de menor a mayor.
Parsort=p.sort()
impsort=im.sort(reverse=True)

print("Pares: ",im.sort(reverse=True))


# Utilizar al menos cuatro de las funciones de listas en python en la lista original de 40 elementos.

# Diccionarios
# Crear un diccionario de 6 personas que conozcas con su primer nombre y su edad.

# Crear una lista con los valores de la edad y reacomodar la lista de menor a mayor valor.

# Usando el diccionario y un loop, imprimir solo los nombres.

# Añadir dos personas nuevas a tu diccionario, incluyendo edad.

# Sets
# Crea un set con 100 numeros aleatorios enteros del 1 al 25.

# Comprueba la longitud de tu set.

# Crea una lista de 5 numeros aleatorios del 1 al 10 y comprueba si cada valor aparece en el set inicial.