nome_completo = input("Digite o nome completo: ").strip()
partes = [p for p in nome_completo.split() if p]

if not partes:
    print("Nenhum nome informado.")
elif len(partes) == 1:
    print(f"Nome: {partes[0].upper()}")
    print("Sobrenome: (não informado)")
else:
    primeiro = partes[0].upper()
    ultimo = partes[-1].upper()
    print(f"Nome: {primeiro}")
    print(f"Sobrenome: {ultimo}")
    