# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:22:43 2023

@author: eliel
"""

'''faca um programa que leia o comprimento do cateto oposto e do 
cateto adjacente de um triangulo retangulo; calcule e mostre o
comprimento da hipotenusa'''

import math

x = int(input("digite o valor do cateto adjascente: "))
y = int(input("digite o valor do cateto oposto: "))
z = math.hypot(x, y)

print("A hipotenusa é: {:.2f}".format(z))
