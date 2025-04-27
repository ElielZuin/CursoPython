# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:02:59 2023

@author: eliel
"""

"""ler o valor em metros e exiba ele convertido em cm e mm"""

#ler o valor em metro:
m = float(input("digite quantos Metros deseja converter: "))
#converter em centimetro:
cm = m*100
#converter em milimetro:
mm= m*1000
#mostrar o valor:
print("{} Metros equivale a: \n{:.0f} Centimetros. \n{:.0f} Milimetros.".format(m, cm ,mm))