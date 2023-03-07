# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:34:49 2023

@author: @author: Ricardo Ismael Gomez Sanchez
"""

#36
num1 = 15
num2 = 20

if num1 < num2:
	print('Se ejecuta el if.')

#37
num1 = 1450
num2 = 60

if num1 != num2:
	print('Se ejecuta el if.')

#38
num1 = 1450
num2 = 60

if num1 == num2:
	print('Se ejecuta el if.')
else:
    print('No entró el if')

#39
color = 'rojo'
if color != 'rojo':
    print ("El color no es rojo.")
else :
    print ("El color es rojo.")
#40
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
    print("Nadie puede tener esa edad.")
elif edad >= 1 and edad <= 18:
    print('Eres un menor de edad.')
elif edad > 18 and edad <= 45:
    print('Eres un adulto.')
elif edad > 45 and edad <= 100:
    print('Eres un adulto mayor.')
elif edad > 100 and edad <= 120:
    print("Eres muy mayor.")
else:
    print('Edad no válida.')

#41
colores = ["rojo", "azul", "verde", "amarillo"]
tupla=tuple(colores)
dat=input("Dame un color:\n")
if dat in tupla :
    print('Dentro')
else:
    print("No lo conosco")