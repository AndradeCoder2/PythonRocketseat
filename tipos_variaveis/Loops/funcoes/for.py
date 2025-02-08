from conda.env.env import print_result

print("Utilizando a função range()")
# Função range() - retorna um intervalo númerico em formato de lista.
# Quando você tem números muito grandes, podemos usar, para não precisarmos fazer a mão.
print(list(range(0,11)))
#  Podemos iterar sobre um intervalo numerico.
for numero in range(5):
 print("Numero:",numero)

print("\nUtilizando a função Len()")
# Função len() - retorna a quantidade de elementos que temos.
lista =[1, 2, 3, 4, 5]
for indice0 in range(0, len(lista)):
    print("Indice 0:", indice0)

#  Acessando o elemento atraves do (indice)
print("\nAcessando o elemento atraves do (Indice):", lista[1])

# Atribuindo e atualizando novo valor atraves do (indice)
print("\nAtribuindo novo valor aos elementos:")
lista2 = [1, 1, 2, 2]
for indice1 in range(0, len(lista2)):
    print("Indice 1:", indice1)
    if indice1 == 3:
        lista2[indice1] = 44
        print(lista2)
