n1= int(input('digite um numero: '))
n2= int(input('digite outro numero: '))
s= n1+n2

#1ª forma de fazer
print('A soma é: ', s)

#formato antigo
print('a soma de ',n1,'+',n2,'é: ',s)

#formato atual e recomendado, USANDO .FORMAT
print('A soma de {} + {} é {}'.format(n1, n2, s))

