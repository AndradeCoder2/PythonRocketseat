print("For utilizando dicionario - keys()")
pessoa = {"Nome": "Paulo Cesar", "Idade": 20, "Cidade": "Cotia"}
for elemento2 in pessoa.keys():
    print(elemento2)

    print("\nFor utilizando dicionario - values()")
    pessoa = {"Nome": "Paulo Cesar", "Idade": 20, "Cidade": "Cotia"}
    for elemento2 in pessoa.keys():
        print(elemento2)

print("\nFor utilizando dicionario - items")
for chave, valor in pessoa.items():
    #  A primeira variavel recebe a (chave) e o segundo o (valor)
    print(f"{chave}: {valor}")
