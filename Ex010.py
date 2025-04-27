# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:03:00 2023

@author: eliel
"""

"""ler quanto dinheiro que uma pessoa tem na carteira e mostre quantos
dolar ela consegue comprar, considere 1dol: 3.27 reais"""

real = float(input("digite a sua quantia de dinheiro em reais: "))
dolar = real / 3.27

print("Voce pode comprar U${:.2f} dol!".format(dolar))