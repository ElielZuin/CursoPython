# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:00:51 2023

@author: eliel
"""

"""crie um algoritimo que leia um numero e mostre o seu dobro
triplo e mostre sua raiz quadrada"""

n = int(input("Digite um numero: "))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print("O dobro de {} é {}, o triplo é {} e a sua raiz quadrada é {:.1f}".format(n, dobro, triplo, raiz))