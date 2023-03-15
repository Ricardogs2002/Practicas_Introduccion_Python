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
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colores[-1])#naranja
print(colores[-7])# amarillo
print(colores[-5])# lila
print(colores[-2])# blanco
print(colores[-10],'\n')# rojo
    
#27
coloresd=colores.copy()
print(colores,'\n')
del coloresd[-9]
del coloresd[3]
del coloresd[-4]
del coloresd[4]
print('del:',coloresd,'\n')

#28
coloresr=colores.copy()
coloresr.remove('amarillo')
coloresr.remove('rojo')
print("remove:",coloresr,'\n')

#29
coloresp=colores.copy()
color1=coloresp.pop(1)
color2=coloresp.pop(7)
colorpop=[color1,color2]
print("pop:",colorpop,'\n')

#30
coloresa=colores.copy()
coloresa.append('fuxia')
coloresa.append('celeste')
print("apend:",coloresa,'\n')

#31
coloresi=colores.copy()
coloresi.insert(6,'magenta')
coloresi.insert(-1,'turquesa')
print("insert:",coloresi,'\n')

#32
coloress=colores.copy()
coloress.sort(reverse=True)
print("sort:",coloress,'\n')

#33
tuplas= ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(tuplas[1])

#34
numero = (10, 1, 5, 11)
print(numero[0]-numero[1]+numero[2]+numero[3])

#35
tupla=tuple(colores)
print(type(tupla),'\n')