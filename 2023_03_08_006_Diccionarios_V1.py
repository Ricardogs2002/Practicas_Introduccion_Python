# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:10:24 2023

@author: Ricardo Ismael Gomez Sanchez
"""

#48
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
print('El teclado',teclado2['Modelo'],"vale $",teclado2['Precio'])

#49
for x in teclado1:
    print(x, '=', teclado1[x] + '.')

#50
del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2['Modelo'])
