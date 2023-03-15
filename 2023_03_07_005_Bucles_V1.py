# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 08:44:55 2023

@author: Ricardo Ismael Gomez Sanchez
"""

#42
x=0
while x<=15:
    print(x)
    x+=5
#43
x=0
while x>=-100:
    print(x)
    x-=20
#44
x=0
while x<=10:
    print("El valor del bucle es:",x)
    x+=1
#45
x=0
while x<=30:
    x+=1
    if x == 4 or x == 6 or x == 10:
        print("Se saltó el valor",x,'de x')
        continue
    print(x)
    if x == 15:
        print("Se rompió en x =",x)
        break
#46
colores = ('rojo','azul','verde','amarillo')
for v in colores:
    print('El color es: ',v)
#47
for x in range(7,700,100):
    print(x)
