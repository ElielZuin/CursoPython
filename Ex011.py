# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:08:24 2023

@author: eliel
"""

"""faca um prog que leia a largura e altura de uma parede em metros
calcule a sua area e a quantidade de tinta necessaria para pintar
sabendo que cada litro de tinta pinta uma area de 2m quadrado"""

#ler altura
alt = int(input("digite a altura em metros: "))
#ler largura
lar = int(input("digite a largura em metros: "))
#calcular a area
area = alt * lar
#quantia de tinta sendo que 1l = 2m²
tinta = area / 2 
#mostrar
print("A sua parede tem {}m² e a quantidade de tinta para pintar a parede é {} litros!".format(area, tinta))