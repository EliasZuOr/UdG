# -*- coding: utf-8 -*-
"""ELIAS ALONSO ZUNIGA OROZCO - Práctica9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gzeWnWsa-XEBFKYBImmdV2sRAWsZfoak

### **Práctica 9**

### **Tema:** Diccionarios

De acuerdo a lo visto en la clase de diccionarios, realice lo que se solicita en los siguientes ejercicios.

**Ejercicio 1**


> 1. Agregue una celda de código y declare un primer diccionario por medio de la función dict() con al menos 3 claves distintas y al menos una de las claves debe contener una lista.
2. Declare un segundo diccionario por medio del uso de llaves {} con al menos 3 claves distintas y al menos una de las claves debe contener una lista.
3. Declare un tercer diccionario a partir de un elemento iterable por medio de la función fromkeys() con al menos 5 claves distintas y el mismo valor inicial.
4. Acceda a todas las claves de cada diccionario declarado por medio de la función keys().
5. Acceda a todos los elementos de cada diccionario declarado por medio de la función values().
6. Acceda al menos a un elemento de cada diccionario por medio de corchetes [].
7. Acceda al valor de una clave de cada diccionario por medio de la función get().
8. A partir de lo anterior, defina un caso predeterminado por si el valor a buscar dentro del diccionario correspondiente no existiera.
9. Acceda al valor de una clave de cada diccionario por medio de la función setdefault().
10. Agregue una nueva clave y un nuevo valor a cada diccionario por medio de la función setdefault().
11. Agregue una nueva clave y valor a cada diccionario por medio de un par clave-valor.
12. Copie la información del primer diccionario declarado a un nuevo diccionario por medio de la función copy().
13. Actualice la información del nuevo diccionario respecto a la información del segundo diccionario declarado por medio de la función update().
14. Borre al nuevo diccionario por medio de la función del().
15. Borre una clave del tercer diccionario por medio de la función del().
16. Borre una clave del tercer diccionario por medio de la función pop().
17. Deje al tercer diccionario vacío por medio de la función clear().
18. Declare un nuevo diccionario a partir de dos listas por medio de la función zip().
19. Verifique la longitud del nuevo diccionario por medio de la función len().
20. Itere sobre todas las claves del nuevo diccionario e imprímalas.
"""

D1 = {'Usuario' : 'Elías', 'Contraseña' : 'Elias2003', 'Estado' : 'Activo'}
D2 = {'Nombre' : 'Elías Alonso Zúñiga Orozco' , 'Edad' : '18 años', 'Telefono' : [3326041801]}
D3 = dict.fromkeys(['A', 'B', 'C', 'D', 'E'], '1')
#4
print(f'{D1.keys()}')
print(f'{D2.keys()}')
print(f'{D3.keys()}')
#5
print(f'{D1.values()}')
print(f'{D2.values()}')
print(f'{D3.values()}')
#6
print(f"{D1['Usuario']}")
print(f"{D2['Nombre']}")
print(f"{D3['A']}")
#7
print(f"{D1.get('Usuario', 'No se encuentra esa clave')}")
print(f"{D2.get('Nombre', 'No se encuentra esa clave')}")
print(f"{D3.get('A', 'No se encuentra esa clave')}")
#8
print(f"{D1.get('Correo', 'No se encuentra esa clave')}")
print(f"{D2.get('Direccion', 'No se encuentra esa clave')}")
print(f"{D3.get('F', 'No se encuentra esa clave')}")
#9
print(f"{D1.setdefault('Usuario', 'No se encuentra esa clave')}")
print(f"{D2.setdefault('Nombre', 'No se encuentra esa clave')}")
print(f"{D3.setdefault('A', 'No se encuentra esa clave')}")
#10
print(f"{D1.setdefault('Correo', 'EliasAloZu03@gmail.com')}")
print(f"{D2.setdefault('Direccion', 'Guadalajara, Jalisco')}")
print(f"{D3.setdefault('F', '1')}")
#11
D1['Registro'] = '11/04/2022'
D2['Calle'] = 'Santo Tomas de Aquino 5322'
D3['G'] = '1'
print(f"{D1['Registro']}")
print(f"{D2['Calle']}")
print(f"{D3['G']}")
#12
D4 = D1.copy()
print(f'{D4}')
#13
D4.update(D2)
print(f'{D4}')
#14
del D4
try: print(f'{D4}')
except: print('Diccionario eliminado')
#15
del D3['A']
print(f'{D3}')
#16
D3.pop('B')
print(f'{D3}')
#17
D3.clear()
print(f'{D3}')
#18
A = ['Nombre', 'RFC', 'Licencia de conducir', 'Escolaridad']
B = ['Elías Alonso Zúñiga Orozco', 'ZUOE030802LU3', 'No', 'Preparatoria']
D5 = dict(zip(A, B))
print(f'{D5}')
#19
print(f'{len(D5)}')
#20
for X in D5:
  print(f'{X} : {D5[X]}')

"""**Ejercicio 2**


> Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves. Imprima al diccionario completo con sus claves y valores.

**Ejemplo de salida en pantalla:**


```
Ingrese un número para el rango: 7

Su diccionario a partir del rango del 1 al 7 es:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

```


"""

N = int(input('Ingrese un número para el rango: '))
D = dict.fromkeys(range(1, N+1))
for X in D:
  D[X] = X**2
print('Su diccionario a partir del rango del 1 al 7 es: ')
print(D)

"""**Ejercicio 3**



> Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntarle al usuario cuantos productos desea registrar y a partir de este dato solicitarle al usuario el artículo y su precio, hecho esto se debe añadir el par (clave, valor) al diccionario. Después se debe mostrar en pantalla el diccionario completo con los articulos y precios, a su vez se deben de sumar los precios de todos los productos e indicarle al usuario cuanto tiene que pagar.

**Ejemplo de salida en pantalla:**



```
Ingrese la cantidad de productos a registrar: 3

Ingrese el nombre del artículo 1: Leche
Ingrese el precio del artículo 1: 35

Ingrese el nombre del artículo 2: Huevo
Ingrese el precio del artículo 2: 60

Ingrese el nombre del artículo 3: Tortillas
Ingrese el precio del artículo 3: 23

Usted lleva los siguientes productos:
{'Leche': 35, 'Huevo': 60, 'Tortillas' : 23}

El pago total es 118 pesos.
```



"""

NP = int(input('Ingrese la cantidad de productos a registrar: '))
P = dict()
D = 0
for X in range(NP):
  A = input(f'Ingrese el nombre del artículo {X+1}: ')
  P[A] = int(input(f'Ingrese el precio del artículo {X+1}: '))
  D += P[A]

print(f'Usted lleva los siguientes productos: {P}')
print(f'El pago total es : ${D} pesos')