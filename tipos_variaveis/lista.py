# Declaração.
minhe_lista = [1, 2, 3, 4, 5, "Rockeseat", True, False]

#  Exibindo uma Lista.
print("minhe lista exemplo", minhe_lista)

# Exibindo os elementos.
print("minhe_lista[0]: ", minhe_lista[0])
print("minhe_lista[1]: ", minhe_lista[1])

print("---------------------------------------------------")

#  Fatiamento, de um elemento a outro elemento (intervalo).
print("minhe_lista[0]: ", minhe_lista[2:7])
print("minhe_lista[0]: ", minhe_lista[1:5])

print("---------------------------------------------------")

#  Fatiamento do começo ate o alvo.
print(minhe_lista[:7])
print(minhe_lista[:4])

print("---------------------------------------------------")

#  Fatiamento do final ate o começo.
print(minhe_lista[2:1])
print(minhe_lista[4:])

print("---------------------------------------------------")

#  Conseguimos alterar o elemento da nossa Lista.
minhe_lista[0] = "Python" # Aqui estamos pegando o indice [0] e modificando ele, tornando ele uma String.
print(minhe_lista)

print("---------------------------------------------------")

""" Metodos de Listas """

#  Metodo append(): ele adicionar um elemento ao final da lista.
minhe_lista.append(6)
print("Apos append(6: )", minhe_lista)

print("---------------------------------------------------")

#  Metodo (index) 
#ele retorna o indice do elemento que quisermos.
indice = minhe_lista.index(5)
print("Indice do elemento 5: ", indice)

print("---------------------------------------------------")

#  Metodo insert: Insere um elemento em um indice expecifico, em uma determinada posição.
minhe_lista.insert(2, 10)
#numero 10 , entrou no lugar do numero 3.
print(minhe_lista)

print("---------------------------------------------------")

#  Metodo (pop). Ele remove e retorna o elemento de um indice especifico.
elemento_removido = minhe_lista.pop(3)
print("Elemento removido ",elemento_removido)

print("---------------------------------------------------")

# Metodo remove, ele remove o elemento
minhe_lista.remove(True)
print("Apos remove(True): ", minhe_lista)

print("---------------------------------------------------")

#  Como organizar nossa lista, ele organiza nossa lista em ordem crescente.
#Metodo (sort), não funciona quando temos elementos de varios tipos.
#Porque estamos tentando ordenar ela em ordem crescente, e não conseguimos fazer isso, com letras.
minhe_lista.sort()
print("Apos short()", minhe_lista)
