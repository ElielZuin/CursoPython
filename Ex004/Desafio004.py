# faça um programa que leia algo pelo teclado e mostre na sua tela o seu
# tipo primitido e a  maior quantidade de informacoes possivel sobre eles.

#fazer com o mozao!

e= input('Digite algo: ')
print('Voce digitou um(a) ',type(e))
print('é alfanumerico? ',e.isalnum())
print('é numerico? ', e.isnumeric())
print('é apenas alfabeto?',e.isalpha())
print('esta em letra maiuscula?',e.isupper())
print('esta em minusculo? ',e.islower())
print('é printavel? ',e.isprintable())
print('so tem espaço? ',e.isspace())

