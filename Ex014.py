# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:03:03 2023

@author: eliel
"""

#faça um programa que informe a temperatura em °C e transforme em °F

#entrada de C
c = float(input("digite quantos °C deseja descobrir em °F: "))

#formula e calculo
f = ((c * 9/5) + 32)

#saida/resultado
print("{:.1f}°C equivale a {:.1f}°F (Graus Fahrenheit)!!!".format(c, f))
