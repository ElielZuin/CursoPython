# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:09:48 2023

@author: eliel
"""

"""faca um algoritmo que leia o preco do produto e mostre seu novo
preco com 5% de desconto"""

produto = float(input("Digite o preco do produto: "))

desc = produto * 0.05           "bastava apenas um np= p - (p * 5 / 100)"
valorfinal = produto - desc

print("Parabens! voce recebeu um desconto de ${:.2f} e seu produto custara apenas ${:.2f}!".format(desc, valorfinal))