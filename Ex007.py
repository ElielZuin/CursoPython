# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:02:55 2023

@author: eliel
"""

"""desenvolva um programa qune leia duas notas do aluno, calcule
e mostre sua media"""


#ler a nota:
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

#calcular a media:
m = (n1 + n2) / 2

#mostrar a media:
print("A media do aluno é: {:.1f}".format(m))