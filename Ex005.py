# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:02:44 2023

@author: eliel
"""

#faca um programa que leia um numero inteiro e mostre na sua
#tela o seu sucessor e antecessor

n = int(input('Digite um Numero: '))
an = n - 1
su = n + 1

print("Voce digitou o numero: {} \nSeu antecessor é: {} \nSeu sucessor é: {}".format(n, an, su))