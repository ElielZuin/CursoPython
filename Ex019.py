# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:22:44 2023

@author: eliel
"""

'''um professor quer sortar um de seus quatro alunos para
apagar o quadro.faca um prog q ajude ele escrevendo o nome deles
e escolhendo um nome'''

from random import choice

n1 = input("digite o primeiro nome: ")
n2 = input("digite o segundo nome: ")
n3 = input("digite o terceiro nome: ")
n4 = input("digite o quartto nome: ")
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("o escolhido foi: ",escolhido)