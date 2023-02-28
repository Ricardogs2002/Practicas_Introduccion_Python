# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:13:19 2023

@author: Ricardo Ismael Gomez Sanchez
"""

#23
colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]
print(colores[3])

#24
i=0
for v in enumerate(colores):
    if colores[i]=="rojo":
        print("El rojo esta en la posición", i)
    if colores[i]=="rosa":
        print("El rosa esta en la posición", i)
    i+=1
#25
numeros = ["tres", "dos", "cinco", "cuatro", "uno"]
print('\n'.join(
    map(lambda v: 'Valor en posicion {}: {}'.format(*v),enumerate(numeros))))

#26


#27


#27


#28

