texto = input("Digite um texto: ")

total = len(texto)
vogais = "aeiouAEIOU" 
qtd_vogais = sum(1 for ch in texto if ch in vogais)

print(f"Total de caracteres: {total}")
print(f"Quantidade de vogais: {qtd_vogais}")
