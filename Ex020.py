# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:22:45 2023

@author: eliel
"""

'''
o mesmo professor quer sortear a ordem de apresentacao dos alunos
faca um prog q leia o nome dos 4 aluno e mostre a ordem sorteada
'''
import random

n1 = input("digite o primeiro aluno: ")
n2 = input("digite o segundo aluno: ")
n3 = input("digite o terceiro aluno: ")
n4 = input("digite o quartto aluno: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("sequencia para apresentar: ")
print(lista)
