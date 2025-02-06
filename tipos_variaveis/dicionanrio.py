#  Criando um dicionario de exemplo.
pessoa = {"nome": "Paulo", "idade": 20, "cidade": "SÃo Paulo"}
print("Meu dicionario de exemplo:", pessoa)

#  Acessando o valor por chave.
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

#  Criando dicionario vazio função ( dict() ).
dicionario_vazio = dict()
print(dicionario_vazio)

#  Atualizar ou Alterar.
pessoa["idade"] = 22
print("Idade:", pessoa["idade"])

#  Removendo um par de chave-valor
del pessoa["idade"]
print(pessoa)


# Metodos Dicionario

""" 
clear()
Usamos para remover todos os elementos do dicionário.
"""
meu_dicionario = {"a": 1, "b": 33, "c": 55}
meu_dicionario.clear()
print(meu_dicionario)

""" 
Keys()
Ele nos mostrara tudo que esta dentro da nossa chave.
Quando usamos, podemos verificar todas as chaves, que temos no nosso dicionario.
"""
chaves = list(pessoa.keys())
print("Chaves do meu dicionario:",chaves)
#Podemos acessar apenas uma chave tambem.
print("Primeira chave:", chaves[1])
# Ao faermos isso ele nos mostrara um ERRO, pois ele (entende que isso não e uma lista direta).
# Para acessarmos devemos, transformar ele uma (lista) fazer um casting.



