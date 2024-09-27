# -*- coding: utf-8 -*-
"""ELIAS ALONSO ZUNIGA OROZCO - Práctica8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14WKO6Jw8xa_YhakrS3yS1Mj_MCq2F0ln

### **Práctica 8**

### **Tema:** Conjuntos

De acuerdo a lo visto en la clase de conjuntos, realice lo que se solicita en los siguientes ejercicios.

**Ejercicio 1**



> 1. Agregue una celda de código y determine 2 conjuntos con al menos 5 elementos distintos cada uno.
2. Declare un tercer conjunto a partir de un objeto iterable
(range).
3. Declare un cuarto conjunto de tipo inmutable por medio de la función frozenset().
4. Evalúe si los elementos 5, ‘A’ y 17 pertenecen a alguno de los 4 conjuntos declarados.
5. Añada un nuevo elemento al primer conjunto por medio de la función add().
6. Elimine a un elemento del segundo conjunto por medio de la función discard().
7. Elimine a un elemento del tercer conjunto por medio de la función remove().
8. Elimine a un elemento del primer conjunto por medio de la función pop().
9. Elimine a todos los elementos del tercer conjunto por medio de la función clear().
10. Verifique la longitud del primer conjunto por medio de la función len().
11. Copie los elementos del segundo conjunto al tercer conjunto por medio de la función copy().
12. Actualice los elementos del primer conjunto con los elementos del segundo conjunto por medio de la función update().
13. Encuentre el valor máximo y mínimo del 1er, 2do y 4to conjunto por medio de las funciones max() y min() respectivamente.
14. Itere sobre todos los elementos del primer conjunto e imprímalos.

**Nota:** Cada instrucción se debe imprimir en pantalla.
"""

#1
A = {'A', 'B', 'C', 'D', 'E'}
B = {'F', 'G', 'H', 'I', 'J'}
#2
C = set(range(5))
#3
D = frozenset({6, 7, 8})
#4
#print((5 or 'A' or 17) in (A or B or C or D))
print('5' in A or B or C or D)
print('A' in A or B or C or D)
print('17' in A or B or C or D)
#5
A.add('F')
#6
B.discard('F')
#7
C.remove(1)
#8
A.pop()
#9
C.clear()
#10
len(A)
#11
#B_Copy = B.copy()
#12

"""**Ejercicio 2**



> 1. Agregue una celda de código y declare los siguientes conjuntos:

    A = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

    B = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

    C = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

> 2. Realice la operación A∪B∪C (unión) e imprima la respuesta.
3. Realice la operación B∩C∩A (intersección) e imprima la respuesta.
4. Realice la operación B\A (diferencia) e imprima la respuesta.
5. Realice la operación C ^ A (diferencia simétrica) e imprima la respuesta.
6. Realice la operación A == B (igualdad) e imprima la respuesta.
7. Indique si B es un subconjunto de A.
8. Indique si C es un superconjunto de B.
9. Indique si A es un conjunto disconexo de B y C.
"""

#1
A = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
B = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
C = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

#2
print(A.union(B.union(C)))

#3
print(A.intersection(B.intersection(C)))

#4
print(B.difference(A))

#5
print(C.symmetric_difference(A))

#6
print(A==B)

#7
print(B.issubset(A))

#8
print(C.issuperset(B))

#9
print(A.isdisjoint(B and C))

"""**Ejercicio 3**


> El congreso "DIVTIC 2022" ofrece los siguientes talleres: Programación en Python, Diseño básico en Inkscape y Manejo básico de Excel. Para cada curso se tiene el siguiente registro de asistentes:


```
Python = {'Alma', 'Gabriel', 'Fernando', 'Perla', 'Marcela', 'Luis'}

Inkscape = {'Pedro', 'Laura', 'Luis', 'Ana', 'Claudia', 'Gabriel'}

Excel = {'Luis', 'José', 'Fátima', 'Carlos', 'Gabriel', 'Graciela'}
```



> De acuerdo al registro realice lo siguiente:


1.   Muestre los nombres de los asistentes que se registraron a los tres cursos.

2.   Muestre los nombres de los asistentes que se registraron solo al curso de Python y no a otro curso.
3.   Muestre los nombres de los asistentes que se registraron solo al curso de Inkscape y no a otro curso.
4.   Muestre los nombres de los asistentes que se registraron solo al curso de Excel y no a otro curso.
5.   Muestre la cantidad total de asistentes al evento y sus nombres.

**Ejemplo de salida en pantalla**

```
Asistentes registrados en los tres talleres: {'Luis', 'Gabriel'}

Asistentes registrados solo en el taller de Python: {'Alma', 'Fernando', 'Perla', 'Marcela'}

Asistentes registrados solo en el taller de Inkscape: {'Pedro', 'Laura', 'Ana', 'Claudia'}

Asistentes registrados solo en el taller de Excel: {'José', 'Fátima', 'Carlos', 'Graciela'}

Total de asistentes al evento: 14

Nombres de los asistentes:  {'Alma', 'Gabriel', 'Fernando', 'Perla', 'Marcela', 'Luis', 'Pedro', 'Laura', 'Ana', 'Claudia', 'José', 'Fátima', 'Carlos','Graciela'}
```




"""

Python = {'Alma', 'Gabriel', 'Fernando', 'Perla', 'Marcela', 'Luis'}
Inkscape = {'Pedro', 'Laura', 'Luis', 'Ana', 'Claudia', 'Gabriel'}
Excel = {'Luis', 'José', 'Fátima', 'Carlos', 'Gabriel', 'Graciela'}
Total = Python.union(Inkscape.union(Excel))

print('Asistentes registrados en los tres talleres: ', Python.intersection(Inkscape.intersection(Excel)))
print('Asistentes registrados solo en el taller de Python: ', Python-Inkscape-Excel)
print('Asistentes registrados solo en el taller de Inkscape: ', Inkscape-Python-Excel)
print('Asistentes registrados solo en el taller de Excel: ', Excel-Python-Inkscape)
print('Total de asistentes al evento: ', len(Total))
print('Nombres de los asistentes: ', Total)