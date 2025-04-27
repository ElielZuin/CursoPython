# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:22:44 2023

@author: eliel
"""

''' ler um angulo qlqr e mostrar na tela o valor do seno, cosseno
e tangente desse angulo'''

import math

ang = float(input("Digite o angulo: "))
g = math.radians(ang)
print("o seno de {} é: {:.2f}".format(ang, math.sin(g)))
print("o cosseno de {} é: {:.2f}".format(ang, math.cos(g)))
print("a tangente de {} é: {:.2f}".format(ang, math.tan(g)))

