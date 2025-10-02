p = input("Digite uma palavra: ").strip().lower()
if p and p == p[::-1]:
    print("É palíndromo.")
else:
    print("Não é palíndromo.")
    