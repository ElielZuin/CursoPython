# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 19:36:52 2023

@author: eliel
"""

from math import sqrt, floor

num = int(input("Digite um número: "))
raiz = sqrt(num)
print("a raiz de {} é igual a {:.2f}".format(num, floor(raiz)))
