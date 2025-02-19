# -*- coding: utf-8 -*-
"""Listas_ParteII.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hzqb3QA5SnWnfZUCgW2mb_1Zrr4vKZ2k

# **TEMA 3.2: LISTAS SEGUNDA PARTE**

**- OPERACIONES EN LISTAS -**

En Python encontramos varios tipos de operaciones que pueden aplicarse a las listas:

*   Longitud
*   Concatenación

*   Repetición
*   Membresía

*   Máximo y mínimo

*   Conteo
*   Reversa
*   Ordenar
*   Copiar

**LONGITUD**

El método len() devuelve el número de elementos que se encuentran en la lista.
"""

# Ejemplo longitud de una lista
lista1, lista2= [10, 20, 30, 40, 50], ['A','a','E','e','I','i','O','o','U','u']
print('Longitud de la lista 1: ', len(lista1))
print('Longitud de la lista 2: ', len(lista2))

"""**CONCATENACIÓN**

La concatenación (+) enlaza dos o más listas y crea una nueva lista a partir de esta unión.
"""

# Ejemplo 1 de concatenación mismo tipo de datos
L1 = [1,2,3]
L2 = [4,5,6]
Nueva_Lista = L1 + L2
print('Nueva lista: ', Nueva_Lista)

# Ejemplo 2 de concatenación tipo de datos diferentes
L3 = ['A','B','C']
L4 = ['¡Hola Mundo!']
Lista_comb = L4 + L1 + L3 + L2
print('Lista combinada: ', Lista_comb)

"""**REPETICIÓN**

La repetición (*) repite una misma lista el número de veces que se le indique y genera una nueva lista a partir de estos datos.
"""

# Ejemplo de repetición
L5 = ['A', 1, 'E', 2, 'I', 3]
Lista_repetida = L5 * 3
print(Lista_repetida)

"""**MEMBRESÍA**

La membresía (in) evalúa si un elemento de la lista es igual a otro elemento externo y devuelve un valor verdadero o falso.
"""

# Ejemplo de membresía
Nombres = ['Vanessa','Gustavo','Miguel']
n = input('Nombre a buscar: ')
print(n,'pertenece a la lista de nombres: ', n in Nombres)

# n in Nombres Si se encuentra el nombre la salida es verdadera
# n not in Nombres Si se encuentra el nombre la salida es falsa

"""**MÁXIMO Y MÍNIMO**

La función max( ) regresa el elemento de la lista con valor máximo.

La función min( ) regresa el elemento de la lista con valor mínimo.

"""

# Ejemplo de valor máximo
Num = [50, 8000, 465, 10300, 1, 0.86, 0.015]
Letra = ['W','G','X','A','Z','Algoritmo','Lista']
print('El número con mayor valor de la lista es: ', max(Num))
print('La letra con mayor valor de la lista es: ', max(Letra))

# Ejemplo de valor mínimo
print('\nEl número con menor valor de la lista es: ', min(Num))
print('La letra con menor valor de la lista es: ', min(Letra))

# Ejemplo palabras con la misma letra
palabras = ['Anillo', 'Ardilla', 'Árbol', 'Avión']
print("\nLa palabra con menor valor de la lista es: ", min(palabras))
print("La palabra con mayor valor de la lista es: ", max(palabras))

"""**CONTEO**

La función count( ) devuelve el recuento de cuántas veces se produce un elemento en la lista.
"""

# Ejemplo de conteo
Lista = ['Lista', 'a', 15, 'e', 'Lista', 15, 987, 16, 15, 'i']
print('Conteo para Lista: ', Lista.count('Lista'))
print('Conteo para 15:    ', Lista.count(15))
print('Conteo para e:     ', Lista.count('e'))
print('Conteo para 3:     ', Lista.count(3))

"""**REVERSA**

El método reverse( ) invierte los elementos de la lista.
"""

# Ejemplo lista al revés
L = [123, 'xyz', 856, 'abc', 'Arturo', 97.65, 0.13]
print('Lista original: ', L)
L.reverse()
print("Lista en reversa: ", L)

"""**ORDENAR**

La función sort( ) ordena una lista de menor a mayor o alfabéticamente según el tipo de datos que contiene.
"""

# Ejemplo 1 ordenar una lista de menor a mayor
LN = [123, 15, 1, 856, 97.65, 0.13, 0.025, 4]
print('Lista original: ', LN)
LN.sort()
print("Lista ordenada: ", LN)

# Ejemplo 2 ordenar una lista de forma alfabética
LA = ['Vanessa','Gustavo','Víctor','Arturo','Itzel','Gabriela','Miguel','Ariana']
print('\nLista original: ', LA)
LA.sort()
print("Lista ordenada: ", LA)

# Ejemplo 3 Lista combinada
LC = ['123', '15', '1', '856', '97.65', '0.13', '0.025', '4', 'Vanessa','Gustavo','Víctor','Arturo']
print('\nLista original: ', LC)
LC.sort()
print("Lista ordenada: ", LC)

"""**COPIAR**

Supongamos que se tiene la siguiente lista y se quiere hacer una copia de esta.

```
Nombres = ['Vanessa','Gustavo','Víctor','Arturo','Itzel']
```

Para hacer una copia de un dato de tipo lista se requiere hacer uso de la función copy(). No se puede hacer una copia de forma directa con el operador de asignación (=) como en el siguiente ejemplo:

```
Nombres2 = Nombres
```

Al hacer esto la variable Nombres2 si guarda los datos de la lista original pero cualquier cambio que se haga en la lista original también se verá reflejado en la lista que "copiamos" mediante el operador de asignación (=). Este caso se ejemplifica en el siguiente código:



"""

Nombres = ['Vanessa','Gustavo','Víctor','Arturo','Itzel']
Nombres2 = Nombres #Se hace una "copia" de la lista original mediante el operador de asignación =

#Se imprime la lista original y la "copia"
print("Lista Original: ", Nombres)
print("Lista Copia: ", Nombres2)

#Remuevo un nombre de la lista original
Nombres.remove("Gustavo")

#Se imprime a la lista original despúes de borrar un nombre y la "copia"
print("\nLista Original: ", Nombres)
print("Lista Copia: ", Nombres2)

"""Note que en el código anterior al aplicar una modificación en la lista original, la lista **"copiada"** mediante el operador de asignación **(=)** también se ve afectada por los mismos cambios.

Para poder copiar una lista y que esta no se vea afectada por los cambios de la lista original, se utilizará a la función copy().
"""

#Función copy()
Nombres = ['Vanessa','Gustavo','Víctor','Arturo','Itzel']
Nombres2 = Nombres.copy() #Se hace una "copia" de la lista original mediante copy()

#Se imprime la lista original y la "copia"
print("Lista Original: ", Nombres)
print("Lista Copia: ", Nombres2)

#Remuevo un nombre de la lista original
Nombres.remove("Gustavo")

#Se imprime a la lista original despúes de borrar un nombre y a la copia
print("\nLista Original: ", Nombres)
print("Lista Copia: ", Nombres2)

"""**- ITERACIÓN DE UNA LISTA -**"""

# Ejemplo Iterar sobre los elementos de una lista

Frutas = ['Arándano', 'Granada', 'Melón', 'Manzana','Pera']
for X in Frutas:
  print(X)

# Ejemplo Iterar sobre las posiciones de una lista por medio de For

for Y in (range(len(Frutas))):
  print(Y, Frutas[Y])

# Ejemplo Iterar sobre las posiciones de una lista por medio de While
F=0
while F < len(Frutas):
  print(F, Frutas[F])
  F = F+1

#Ejemplo de como solicitar elementos y guardarlos en una lista
LV = []

dato = input("Ingresa una palabra: ")
dato = dato.upper() #Mayúsculas
LV.append(dato)

dato = input("Ingresa una palabra: ")
dato = dato.lower() #Minúsculas
LV.append(dato)

print(LV)

L = []
n = int(input("Cuantos elementos desea ingresar: "))
for i in (range(n)):
  dato = input("Ingresa una palabra: ")
  L.append(dato)

print(L)