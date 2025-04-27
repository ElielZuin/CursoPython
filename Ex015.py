# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:03:05 2023

@author: eliel
"""

"""
Faca um prog que pergunte quantos dias o carro foi alugado e quantos kms ele
rodou, levando em consideracao que custa 60conto por dia e 15centavos por km e mostre
o valor final do aluguel em rs
"""

dia = int(input("digite a quantidade de dias que ficou com o veículo: "))
km = int(input("digite a quantidade de kilometros que voce rodou com o carro: "))

pdia = dia * 60
pkm = km * 0.15
pfinal = pdia + pkm
# o professor usou: preco = (dia * 60) + (km * 0.15)

print("O preço pelos dias sao R${:.2f}".format(pdia))
print("O preço pelos KM's é de R${:.2f}".format(pkm))
print("O preço total pelo aluguel é R${:.2f}".format(pfinal))
