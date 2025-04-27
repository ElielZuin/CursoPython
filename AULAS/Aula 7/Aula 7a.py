n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
m = n1 * n2 
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {},\n o produto é {}, e a divisao é {:.3f}'.format(s,m,d), end=' ')
print('Divisao inteira {}, e potencia {}'.format(di, e))