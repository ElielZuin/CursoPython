# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:20:58 2023

@author: eliel
"""

'''crie um programa que leia um numero real e mostre na sua tela
a sua porcao inteira'''

import math

n = float(input("digite um numero real: "))
print("a porcao inteira de {} é: {}".format(n, math.trunc(n)))
