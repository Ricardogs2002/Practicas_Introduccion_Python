# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:53:32 2023

@author: Ricardo Ismael Gomez Sanchez
"""

#51
def suma(n1, n2):
    print(n1 + n2)
suma(15, 15)
suma(25, 25)
suma(30000, 27000)

#52
def colores(*args):
    print("La llamada tiene",len(args),'argumentos')

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

#53
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('negro',"amarillo")

#54
def suma(*args):
    resultado = args[0] + args[1] + args[2] + args[3] + args[4]
    print('El resultado de sumar estos cinco números es:', resultado)
suma(3, 9, 54, 5786, 6, 8)
