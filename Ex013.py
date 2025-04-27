# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:10:01 2023

@author: eliel
"""

"""ler o salario do funcionario e depois mostrar seu novo salario
com 15% de aumento"""

sal = int(input("Digite o salario atual do funcionário: "))
aum = sal * 0.15
salfinal = sal + aum
print("Voce recebeu um aumento de {}! seu novo salario é de R${}!!!!!".format(aum, salfinal))
